# This script traverses all the valid projects, creates a csv for the input for pa tool and writes the points in the
# following form: project, commit, benchmark, params, instance, trial, fork, iteration, mode, unit, value_count, value

# At the end the output file's location is written to pa_input_projects.csv so that we can iterate in the folder to calculate RCIW later

import csv, calculation, sys, os

go_results_path = sys.argv[1]



with open('go_results_valid/go-results-2-valid.csv', 'r') as results_file:
    results_file.readline()  # get rid of title
    results_file_reader = csv.reader(results_file)
    with open(f'{go_results_path}/cumulus-1/go-projects.csv', 'r') as names_file:
        names_file.readline()  # get rid of title
        names_file_reader = csv.reader(names_file)
        name_counter = 0
        for row_result in results_file_reader:      # iterating through all valid projects
            for row_name in names_file_reader:      # iterating through names of projects
                if row_result[3] == row_name[2]:    # looking if the commits are the same
                    name_counter += 1
                    print(name_counter)
                    name = row_name[0]
                    path = f'{go_results_path}/' + row_result[0] + "/results-c1-" + row_result[3] + ".csv"
                    commit = row_result[3]
                    data_points = calculation.create_bench_dict(path)
                    sorted_benchmark_names = sorted(data_points.keys())
                    print(sorted_benchmark_names)
                    print("\n")
                    #
                    name_splitted = name.split('/')
                    if not os.path.exists('pa_input_projects'):
                        os.mkdir('pa_input_projects')
                    outfile_name = f"pa_input_projects/{name_counter}&{name_splitted[0]}&{name_splitted[1]}_benchmarks.csv"
                    outfile = open(outfile_name, 'a', newline='')
                    outfile_writer = csv.writer(outfile, delimiter=';')
                    outfile_writer.writerow(['project', 'commit', 'benchmark', 'params', 'instance', 'trial', 'fork', 'iteration', 'mode', 'unit', 'value_count', 'value'])
                    for benchmark_name in sorted_benchmark_names:
                        trial = 0
                        for data_point in data_points[benchmark_name]:
                            outfile_writer.writerow([name, commit, benchmark_name,'', 0, trial, 0, 0, '', '', 1, data_point])
                            trial += 1
                    outfile.close()
                    #
                    folder_iterator = open('pa_input_projects.csv', 'a', newline='')
                    folder_iterator.write(outfile_name+'\n')
                    folder_iterator.close()
                    names_file.seek(0)
                    break
