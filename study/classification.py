from collections import namedtuple
import csv
import time

import numpy as np
import pandas as pd
import pendulum
from tqdm import tqdm

from imblearn.over_sampling import SMOTE
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import RepeatedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from conf_independent_variables import INDEPENDENT_VARIABLES
from conf_models import get_classification_models
from conf_scores import compute_multiple_scores
from conf_selectors import AutoSpearmanSelector
from utils import apply_binary_threshold, approximate_zeros, PandasSelector, PandasTransformer, remove_negative_values



ITERATIONS_DATA_FILE_PATHS = [
    (5, 'resources/variabilities_5_iterations.csv'),
    (10, 'resources/variabilities_10_iterations.csv'),
    (20, 'resources/variabilities_20_iterations.csv'),
    (30, 'resources/variabilities_30_iterations.csv'),
]
RESULTS_OUTPUT_CSV_FILE_PATH = 'resources/output/classification_results.csv'
FEATURES_OUTPUT_CSV_FILE_PATH = 'resources/output/classification_features.csv'

RANDOM_SEED = 42

CROSS_VALIDATION_FOLDS = 10
CROSS_VALIDATION_REPETITIONS = 30
CROSS_VALIDATION_GENERATOR = RepeatedKFold(
    n_splits=CROSS_VALIDATION_FOLDS,
    n_repeats=CROSS_VALIDATION_REPETITIONS,
    random_state=RANDOM_SEED,
)
TOTAL_CROSS_VALIDATION_FOLDS = CROSS_VALIDATION_FOLDS * CROSS_VALIDATION_REPETITIONS

DEPENDENT_VARIABLES = [
    'rciw99',
    'rciw99mjhd',
    'rmadhd',
]

BINARY_CLASSIFICATION_THRESHOLDS = [
    1,
    3,
    5,
    10,
]

MODELS = get_classification_models(RANDOM_SEED)

SELECTORS = [
    ('None', None),
    ('AutoSpearmanSelector()', PandasSelector(AutoSpearmanSelector(clustering_threshold=0.7, vif_threshold=5))),
]

SAMPLERS = [
    ('None', None),
    ('SMOTE()', SMOTE(random_state=RANDOM_SEED)),
]

EvaluationRow = namedtuple(
    'EvaluationRow', (
        'dependent_variable',
        'iterations',
        'threshold',
        'selector',
        'sampler',
        'model',
        'fold',
        'precision',
        'recall',
        'accuracy',
        'fmeasure',
        'auc',
        'mcc',
        'train_time',
    )
)

FEATURES_CSV_HEADER = ['dependent_variable', 'iterations', 'threshold', 'selector', 'fold'] + INDEPENDENT_VARIABLES



def main():
    # Create the output file.
    results_df = pd.DataFrame.from_records([], columns=EvaluationRow._fields)
    results_df.to_csv(RESULTS_OUTPUT_CSV_FILE_PATH, mode='w', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n', index=False)

    # Create the features file.
    features_df = pd.DataFrame.from_records([], columns=FEATURES_CSV_HEADER)
    features_df.to_csv(FEATURES_OUTPUT_CSV_FILE_PATH, mode='w', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n', index=False)

    # Iterates over the iterations data files.
    for iterations, file_path in tqdm(ITERATIONS_DATA_FILE_PATHS, desc='Iterations'):
        # Read the data from CSV.
        df_original = pd.read_csv(file_path)

        # Iterates over the dependent variables
        for dep_var in tqdm(DEPENDENT_VARIABLES, leave=False, desc='Dependent variables'):
            # Make a copy of the raw dataset.
            df = df_original.copy()

            # Clean the data from negative values.
            df = remove_negative_values(df, dep_var)

            # Clean the data from 0 values.
            df = approximate_zeros(df, dep_var)

            # Select X and y.
            X = df[INDEPENDENT_VARIABLES]
            y = df[dep_var]

            # Iterate the threshold values.
            for threshold in tqdm(BINARY_CLASSIFICATION_THRESHOLDS, leave=False, desc='Thresholds'):
                # Transform into a binary classification problem (0: stable, 1: unstable).
                # Stable: [0, threshold], Unstable: (threshold, inf]
                y_binary = apply_binary_threshold(y, threshold)

                # Iterate the feature subset selectors.
                for selector_name, selector in tqdm(SELECTORS, desc='Selectors'):
                    # Iterate the folds.
                    for fold, (train_indexes, test_indexes) in tqdm(enumerate(CROSS_VALIDATION_GENERATOR.split(X, y_binary)), total=TOTAL_CROSS_VALIDATION_FOLDS, leave=False, desc='Folds'):
                        # Retrieve the split data.
                        X_train, y_train = X.iloc[train_indexes], y_binary.iloc[train_indexes]
                        X_test, y_test = X.iloc[test_indexes], y_binary.iloc[test_indexes]

                        # Preprocess the data.
                        preprocess_pipeline = Pipeline([
                            ('scaler', PandasTransformer(StandardScaler())),
                            ('selector_1', PandasSelector(VarianceThreshold())),
                            ('selector_2', selector),
                        ])
                        # Fit on the train.
                        X_pp_train = preprocess_pipeline.fit_transform(X_train)
                        # Only transform on the test.
                        X_pp_test = preprocess_pipeline.transform(X_test)

                        # Retrieve the features mask.
                        features_mask = {x: x in X_pp_train.columns for x in INDEPENDENT_VARIABLES}

                        # Save the features.
                        features_df = pd.DataFrame.from_records([{
                            'dependent_variable': dep_var,
                            'iterations': iterations,
                            'threshold': threshold,
                            'selector': selector_name,
                            'fold': fold,
                            **features_mask,
                        }], columns=FEATURES_CSV_HEADER)
                        features_df.to_csv(FEATURES_OUTPUT_CSV_FILE_PATH, mode='a', header=False, quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n', index=False)

                        # Iterate the samplers.
                        for sampler_name, sampler in tqdm(SAMPLERS, leave=False, desc='Samplers'):
                            # Apply the resampling method, if any.
                            if sampler:
                                X_pp_resampled_train, y_pp_resampled_train = sampler.fit_resample(X_pp_train, y_train)
                            else:
                                X_pp_resampled_train, y_pp_resampled_train = X_pp_train.copy(), y_train.copy()

                            # Iterate the models.
                            for classifier_name, classifier in tqdm(MODELS, leave=False, desc='Models'):
                                tqdm.write(f'dependent_variable={dep_var}, iterations={iterations}, threshold={threshold}, selector={selector_name}, sampler={sampler_name}, fold={fold}, model={classifier_name}')

                                # Train the model.
                                fit_start_time = time.time()
                                classifier.fit(X_pp_resampled_train, y_pp_resampled_train)
                                fit_time = time.time() - fit_start_time

                                # Get the scores against the test data.
                                scores = compute_multiple_scores(classifier, X_pp_test, y_test)

                                # Store the results.
                                evaluation_row = EvaluationRow(
                                    dependent_variable=dep_var,
                                    iterations=iterations,
                                    threshold=threshold,
                                    selector=selector_name,
                                    sampler=sampler_name,
                                    model=classifier_name,
                                    fold=fold,
                                    precision=scores['precision'],
                                    recall=scores['recall'],
                                    accuracy=scores['accuracy'],
                                    fmeasure=scores['fmeasure'],
                                    auc=scores['auc'],
                                    mcc=scores['mcc'],
                                    train_time=fit_time,
                                )

                                # Save the results.
                                results_df = pd.DataFrame.from_records([evaluation_row], columns=EvaluationRow._fields)
                                results_df.to_csv(RESULTS_OUTPUT_CSV_FILE_PATH, mode='a', header=False, quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n', index=False)



if __name__ == '__main__':
    start_time = pendulum.now()
    main()
    print(f'Execution time: {(pendulum.now() - start_time).in_words()}')
