# Approach Scripts and Data

This subfolder contains the scripts and data extracted by our approach, without the machine learning part.

## Installation
The following software is required to be installed
* [Go](https://golang.org)
* [Python 3](https://www.python.org/)
* [*pa*](https://github.com/chrstphlbr/pa) tool



Although each folder has their own READMEs inside, here is a short explanation about which folder is used for what purpose:

## BenchmarkVariabilities
BenchmarkVariabilities (in folder `BenchmarkVariabilities`) transforms the raw execution data into the benchmark variabilities.
1. takes as input the raw execution data from the projects (in `go_results/`)
2. filters the valid projects with `1-filter_valid_projects.py` and creates `go-results-valid/go-results-2-valid.csv`,
3. creates the input to the [*pa*](https://github.com/chrstphlbr/pa) tool with `3-inputcsvcreator.py` found in `pa_input_projects/`
4. creates the variability files for a number of iterations with *pa* by running `4-get_pa_results_iteration.py`.
Files for 5, 10, and 20 iterations are named `final_5_iterations.csv`, `final_10_iterations.csv`, and `final_20_iterations.csv`, respectively.



## BenchmarkProjects
Downloader script written in Python, takes "project_commit.csv" from BenchmarkVariabilites (run `python BenchmarkVariabilities/project_commit.py`) to download according projects.
It creates the input for the feature extraction (in folder `FeatureExtraction`).



## FeatureExtraction
FeatureExtraction (in folder `FeatureExtraction`) extracts and combines features as described in the paper.
It includes
* a dependency fetcher for the downloaded projects (`cmd/deps/`),
* the AST feature parser (`cmd/ast/`),
and
* the call graph feature combiner (`cmd/cg/`).
How to use them are explained in its own README file with instrucstions on how to build and execute them.
These take as input "project_commit_place.csv" from BenchmarkProjects.



## MergeFiles
MergeFiles (in folder `MergeFiles`) merges individual output files from FeatureExtraction and BenchmarkVariabilities.
The reuslting, merged files include the features and the variabilties, which are the input for the machine learning part of our approach.
