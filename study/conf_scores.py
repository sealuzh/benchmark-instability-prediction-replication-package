import warnings

import numpy as np

from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score, f1_score, matthews_corrcoef, precision_score, recall_score, roc_auc_score



def mcc_score(y_true, y_pred):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=RuntimeWarning)
        return matthews_corrcoef(y_true, y_pred)

def auc_score(y_true, y_pred):
    try:
        return roc_auc_score(y_true, y_pred)
    except ValueError:
        return 0.0

PRECISION_SCORER = make_scorer(precision_score, zero_division=0)
RECALL_SCORER = make_scorer(recall_score, zero_division=0)
ACCURACY_SCORER = make_scorer(accuracy_score)
FMEASURE_SCORER = make_scorer(f1_score, zero_division=0)
AUC_SCORER = make_scorer(auc_score, needs_proba=True)
MCC_SCORER = make_scorer(mcc_score)

SCORES = [
    ('precision', PRECISION_SCORER),
    ('recall', RECALL_SCORER),
    ('accuracy', ACCURACY_SCORER),
    ('fmeasure', FMEASURE_SCORER),
    ('auc', AUC_SCORER),
    ('mcc', MCC_SCORER),
]


def compute_multiple_scores(estimator, X, y_true, scores=SCORES):
    result = {}
    for score_name, score_function in scores:
        score = score_function(estimator, X, y_true)
        result[score_name] = score
    return result
