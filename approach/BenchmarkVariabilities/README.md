Given is the folder called "go_results", which includes the results of open source Go projects' benchmarks. Looking at
the file "go-results-2.csv"(this file includes commits), we are interested in commit1-results of these projects.

How this python tool works:
1. `1-filter_valid_projects.py` looks at the c1 results in "go-results-2.csv" and saves all the rows that have a value greater
than 0 into a new file called "go-results-2-valid.csv" into the folder "go_results_valid".

Give path of the "go_results" folder.
HOW TO RUN: `python 1-filter_valid_projects PATH`

1. `3-inputcsvcreater.py` iterates through valid projects defined in "go_results_valid/go-results-2-valid.csv" and creates a pa-tool compatible
input csv file for each project that are stored in the folder "pa_input_projects", so that we can give these csv files to pa tool to get the RCIW values.
Also the paths of these csv files are stored in the file "pa_input_projects.csv" to iterate through paths when using pa tool.

Give path of the "go_results" folder.
HOW TO RUN: `python 3-inputcsvcreater.py PATH`

1. `4-get_pa_result_iteration.py` iterates through all projects defined in "pa_input_projects.csv" and gives them as input to pa-tool.
From the output of pa-tool, the RCIW values are acquired from stdin and mean, cv values are added to each benchmark. Finally,
these are written to final.csv which is ready to be visualized/analyzed.

Give path of the pa-tool and the number of iterations for variability calculation (in the paper 5, 10, and 20).
HOW TO RUN: `python 4-get_pa_result.py PATH_TO_PA NR_ITERATIONS`
