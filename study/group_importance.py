from collections import namedtuple
import csv
import time

import numpy as np
import pandas as pd
import pendulum
from tqdm import tqdm

from sklearn.model_selection import RepeatedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from conf_independent_variables import INDEPENDENT_VARIABLES, IV_GROUPS
from conf_models import get_group_importance_models
from conf_scores import compute_multiple_scores
from conf_selectors import ExcludeColumnsSelector
from utils import approximate_zeros, PandasSelector, PandasTransformer, remove_negative_values



ITERATIONS_DATA_FILE_PATHS = [
    (30, 'resources/variabilities_30_iterations.csv'),
]

RESULTS_OUTPUT_CSV_FILE_PATH = 'resources/output/group_importance_mcc_results.csv'

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

BINARY_CLASSIFICATION_THRESHOLDS = [10]

MODELS = get_group_importance_models(RANDOM_SEED)

SELECTORS = [(group_name, ExcludeColumnsSelector(columns=group)) for group_name, group in IV_GROUPS]

EvaluationRow = namedtuple(
    'EvaluationRow', (
        'dependent_variable',
        'iterations',
        'threshold',
        'excluded_group',
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



def main():
    # Create the output file.
    results_df = pd.DataFrame.from_records([], columns=EvaluationRow._fields)
    results_df.to_csv(RESULTS_OUTPUT_CSV_FILE_PATH, mode='w', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n', index=False)

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
                y_binary = pd.cut(y, bins=[0, threshold, np.inf], labels=[0, 1])

                # Iterate the feature subset selectors.
                for group_name, selector in tqdm(SELECTORS, desc='Selectors'):
                    # Iterate the folds.
                    for fold, (train_indexes, test_indexes) in tqdm(enumerate(CROSS_VALIDATION_GENERATOR.split(X, y_binary)), total=TOTAL_CROSS_VALIDATION_FOLDS, leave=False, desc='Folds'):
                        # Retrieve the split data.
                        X_train, y_train = X.iloc[train_indexes], y_binary.iloc[train_indexes]
                        X_test, y_test = X.iloc[test_indexes], y_binary.iloc[test_indexes]

                        # Preprocess the data.
                        preprocess_pipeline = Pipeline([
                            ('scaler', PandasTransformer(StandardScaler())),
                            ('selector', PandasSelector(selector)),
                        ])
                        # Fit on the train.
                        X_pp_train = preprocess_pipeline.fit_transform(X_train)
                        # Only transform on the test.
                        X_pp_test = preprocess_pipeline.transform(X_test)

                        # Iterates the models.
                        for classifier_name, classifier in tqdm(MODELS, leave=False, desc='Models'):
                            tqdm.write(f'dependent_variable={dep_var}, iterations={iterations}, threshold={threshold}, excluded_group={group_name}, fold={fold}, model={classifier_name}')

                            # Train the model.
                            fit_start_time = time.time()
                            classifier.fit(X_pp_train, y_train)
                            fit_time = time.time() - fit_start_time

                            # Get the scores against the test data.
                            scores = compute_multiple_scores(classifier, X_pp_test, y_test)

                            # Store the results.
                            evaluation_row = EvaluationRow(
                                dependent_variable=dep_var,
                                iterations=iterations,
                                threshold=threshold,
                                excluded_group=group_name,
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
