METRICS_LABELS = {
    'precision': 'Precision',
    'recall': 'Recall',
    'fmeasure': 'F-measure',
    'auc': 'AUC',
    'mcc': 'MCC',
}

MODELS_LABELS = {
    'DummyClassifier(strategy=\'most_frequent\')': 'BM',
    'DummyClassifier(strategy=\'prior\')': 'BP',
    'DummyClassifier(strategy=\'stratified\')': 'BS',
    'DummyClassifier(strategy=\'uniform\')': 'BU',
    'AdaBoostClassifier()': 'AB',
    'DecisionTreeClassifier()': 'DT',
    'GaussianNB()': 'NB',
    'GradientBoostingClassifier()': 'GB',
    'KNeighborsClassifier()': 'KNN',
    'LinearDiscriminantAnalysis()': 'LDA',
    'LogisticRegression()': 'LR',
    'MLPClassifier()': 'NN',
    'RandomForestClassifier()': 'RF',
    'SVC(kernel=\'linear\')': 'LSVM',
    'SVC(kernel=\'rbf\')': 'RSVM',
}

SELECTORS_LABELS = {
    'None': 'None',
    'AutoSpearmanSelector()': 'AutoSpearman',
}

SAMPLERS_LABELS = {
    'None': 'None',
    'SMOTE()': 'SMOTE',
}

PREPROCESSING_GROUPS_LABELS = {
    'None/None': f'{SELECTORS_LABELS["None"]}/{SAMPLERS_LABELS["None"]}',
    'None/SMOTE()': f'{SELECTORS_LABELS["None"]}/{SAMPLERS_LABELS["SMOTE()"]}',
    'AutoSpearmanSelector()/None': f'{SELECTORS_LABELS["AutoSpearmanSelector()"]}/{SAMPLERS_LABELS["None"]}',
    'AutoSpearmanSelector()/SMOTE()': f'{SELECTORS_LABELS["AutoSpearmanSelector()"]}/{SAMPLERS_LABELS["SMOTE()"]}',
}

MAGNITUDE_LABELS = {
    'negligible': 'N',
    'small': 'S',
    'medium': 'M',
    'large': 'L',
}
