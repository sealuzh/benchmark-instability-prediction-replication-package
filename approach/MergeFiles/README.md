# Combining Features and Merging with Variabilities

For the analysis to work, the following files need to be in the same folder as the analysis Python files:
* `final_i_iteration.csv` from `BenchmarkVariabilities`, where `i` is the number of iterations
* `csv1` and `csv2` folders from `FeatureExtraction`


## Combining features into one file
* `csv1_combiner.py` combines found benchmarks in `csv1` folder into  `csv1.csv`
* `csv2_combiner.py` combines found benchmarks in `csv2` folder into `benchmark_properties.csv`
* `merge_csv1_csv2.py` merges `csv1.csv` and `benchmark_properties.csv` into a single file `benchmark_properties_valid.csv`.

## Creating files with features and variabilities
* `merge_features_variabilities.py` merges the valid feature file with the variability file into `merged_valid_i_iterations.csv` where `i` is the number of iterations.
Run: `python merge_features_variabilities i` where `i` is the number of iterations
