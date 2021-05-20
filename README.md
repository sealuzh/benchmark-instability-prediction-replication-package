[![DOI](https://zenodo.org/badge/{369158102}.svg)](https://zenodo.org/badge/latestdoi/369158102)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)(http://creativecommons.org/licenses/by/4.0/)

# Predicting Unstable Software Benchmarks Using Static Source Code Features

## Replication package

This replication package can be used to replicate the study we performed
in our paper with the title *Predicting Unstable Software Benchmarks Using Static Source Code Features* authored by Christoph Laaber, Mikael Basmaci, and Pasquale Salza.

This replication package is also available on GitHub:  [sealuzh/benchmark-instability-prediction-replication-package](https://github.com/sealuzh/benchmark-instability-prediction-replication-package).


### Approach
[`approach/`](approach/) contains all data and scripts of our approach, including feature extraction and combination, variability computation, and generating the resulting files for the machine learning part in [`study/`](study/).
The approach's [README](approach/README.md) contains detailed information.


### Study

[`study/`](study/) contains the majority of the data and scripts to completely reproduce the study we conducted to evaluate our approach.

[`r_analyses/`](r_analyses/) contains the data and scripts for running the individual feature analysis of RQ 2 as well as the scripts for creating the scatter plot of Figure 2.

[`resources/variabilities_5_iterations.csv`](study/resources/variabilities_5_iterations.csv),
[`resources/variabilities_10_iterations.csv`](study/resources/variabilities_10_iterations.csv),
[`resources/variabilities_20_iterations.csv`](study/resources/variabilities_20_iterations.csv),
and
[`resources/variabilities_30_iterations.csv`](study/resources/variabilities_30_iterations.csv) are the files containing the data we collected by running the benchmarks, with a number of iterations of `5`, `10`, `20`, and `30`, respectively.

## Classification (RQ 1)
* [`classification.py`](study/classification.py) is a *Python* script to run all the experiments to train the machine learning models and evaluate their performance.
* [`resources/classification_results.csv.xz`](study/resources/classification_results.csv.xz) is the outcome of the previous step, containing all the computed metrics for all the combinations of machine learning algorithm, number of iterations, threshold, and fold.
* [`classification_study.ipynb`](study/classification_study.ipynb) is a *Jupyter Notebook* we used to study the prediction performance of our approach.

## Feature Importance (RQ 2)

### Individual Features
* [`feature_importance.py`](study/feature_importance.py) is a *Python* script to run the permutation feature importance of individual features.
* [`resources/feature_importance_mcc_results.csv`](study/resources/feature_importance_mcc_results.csv) is the outcome of the previous step, containing all MCC feature importances for each variability measure (RCIW Maritz-Jarrett, RCIW bootstrap, and RMAD) and each fold.
We also provide feature importances for other prediction preformances metrics, i.e., AUC and F-measure.
* [`individual_feature_importance.R`](r_analyses/individual_feature_importance.R) is an R script to run the individual feature analyses and plot Figure 10.
To plot the figure, run the R function `run`.
To get statistics, run the R function `run_individual_features_stats`.

### Feature Categories
* [`group_importance.py`](study/group_importance.py) is a *Python* script to run the feature importance for feature categories.
* [`resources/group_importance_mcc_results.csv`](study/resources/group_importance_mcc_results.csv) is the outcome of the previous step, containing all feature importances for each feature category, variability measure (RCIW Maritz-Jarrett, RCIW bootstrap, and RMAD), and fold.
* [`group_importance_study.ipynb`](study/group_importance_study.ipynb) is a *Jupyter Notebook* we used to study the feature importance of feature categories.

For Jupyter Notebooks, we also provide the compiled *HTML* file with included output.
