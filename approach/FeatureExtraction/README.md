This Go projects 3 mains:
1. Dependency fetcher for projects
2. AST feature extraction (extracts source code features from all functions of a project and saves it in a .csv file
3. Call graph feature combination (runs a callgraph analysis on the projects, which are in the output of AST features, to cumulate feature values for benchmarks.
                        It then saves the benchmarks of a project with their values to a .csv file)


Usage:
* Dependency fetcher (This will fetch the dependencies for the projects) [1) Go get 2) GoABS deps.Fetch]
to build it from cmd/deps --> `go build`
to run it --> give path of "project_commit_place.csv" from downloaderscript
`./deps "BenchmarkProjects/project_commit_place.csv"`



* AST feature extraction
to build it from cmd/ast --> `go build`
to run it --> give the path of "project_commit_place.csv" from downloaderscript
`./ast "BenchmarkProjects/project_commit_place.csv"`

Output: csv1 folder --> every project's csv file
                        index.csv showing the files (name, project_csv, project_path)
        these are for call graph feature combination



* Call graph feature combination
to build it from cmd/cg --> `go build`
to run it --> just run the call graph feature combination, it will read index.csv from csv1 and iterate through projects to cumulatively collect feature values
`./cg`

Output: csv2 folder --> every project's csv file
                        index.csv showing the files (name, project_csv, project_path)



