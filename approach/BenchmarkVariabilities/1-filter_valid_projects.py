# This file is to extract projects with valid results from the go-results-2.csv file

# Steps to go:
# 1) Read go-results-2.csv
# 2) For each line, check if c1_results is > 0. If this is the case, write the whole line to another csv file.
# 3) Save the final csv to later read all the projects' benchmarks' values.

import csv, os, sys

go_results_path = sys.argv[1]

with open(f'{go_results_path}/go-results-2.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    title = next(csv_reader)
    if not os.path.exists('go_results_valid'):
        os.mkdir('go_results_valid')
    with open('go_results_valid/go-results-2-valid.csv', mode='a', newline='') as new_file:
        valid_writer = csv.writer(new_file, delimiter=',')
        valid_writer.writerow(title)
        for row in csv_reader:
            if (int(row[4]) is not None) and int(row[4]) > 0:
                valid_writer.writerow(row)
                print(row)

# Gives 230 projects into a new csv file
