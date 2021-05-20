run `python downloadProjects.py`

This is the downloader script for the Go projects.

Usage:
1. get project_commit.csv from BenchmarkVariabilities project
2. run downloader and specify a path to download projects (this will automatically create GOPATH while downloading)
	$ python downloadProjects "place_to_download"
	you can use ./ if you want to download projects in the same folder
3. it will download projects and will give an output as "project_commit_place.csv" for the FeatureExtraction to iterate projects and extract source code features.