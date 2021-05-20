from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def get_classification_models(random_seed):
    return [
        (
            'AdaBoostClassifier()',  # Adaptive Boosting (AdaBoost)
            AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=3, random_state=random_seed), random_state=random_seed),
        ),
        (
            'DecisionTreeClassifier()',  # Decision Tree (DT)
            DecisionTreeClassifier(random_state=random_seed),
        ),
        (
            'DummyClassifier(strategy=\'most_frequent\')',
            DummyClassifier(strategy='most_frequent', random_state=random_seed),
        ),
        (
            'DummyClassifier(strategy=\'prior\')',
            DummyClassifier(strategy='prior', random_state=random_seed),
        ),
        (
            'DummyClassifier(strategy=\'stratified\')',
            DummyClassifier(strategy='stratified', random_state=random_seed),
        ),
        (
            'DummyClassifier(strategy=\'uniform\')',
            DummyClassifier(strategy='uniform', random_state=random_seed),
        ),
        (
            'GaussianNB()',  # Naive Bayes (NB)
            GaussianNB(),
        ),
        (
            'GradientBoostingClassifier()',  # Gradient Boosting Machine (GBM)
            GradientBoostingClassifier(random_state=random_seed),
        ),
        (
            'KNeighborsClassifier()',  # k-NearestNeighbour (KNN)
            KNeighborsClassifier(),
        ),
        (
            'LinearDiscriminantAnalysis()',  # Linear Discriminant Analysis (LDA)
            LinearDiscriminantAnalysis(),
        ),
        (
            'LogisticRegression()',  # Logistic Regression
            LogisticRegression(max_iter=100000, random_state=random_seed),
        ),
        (
            'MLPClassifier()',  # Multi-Layer Perceptron Neural Network
            MLPClassifier(max_iter=100000, random_state=random_seed),
        ),
        (
            'QuadraticDiscriminantAnalysis()',  # Quadratic Discriminant Analysis (QDA)
            QuadraticDiscriminantAnalysis(),
        ),
        (
            'RandomForestClassifier()',  # Random Forest (RF)
            RandomForestClassifier(random_state=random_seed),
        ),
        (
            'SVC(kernel=\'linear\')',  # Support Vector Machine with linear kernel (LinearSVM)
            SVC(kernel='linear', max_iter=100000, probability=True, random_state=random_seed),
        ),
        (
            'SVC(kernel=\'rbf\')',  # Support Vector Machine with radial kernel (RadialSVM)
            SVC(kernel='rbf', max_iter=100000, probability=True, random_state=random_seed),
        ),
    ]


def get_group_importance_models(random_seed):
    return [
        (
            'RandomForestClassifier()',  # Random Forest (RF)
            RandomForestClassifier(random_state=random_seed),
        ),
    ]


def get_feature_importance_models(random_seed):
    return [
        (
            'RandomForestClassifier()',  # Random Forest (RF)
            RandomForestClassifier(random_state=random_seed),
        ),
    ]
