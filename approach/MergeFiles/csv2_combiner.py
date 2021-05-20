import csv

with open("benchmark_properties.csv", 'w', encoding='utf-8', newline='') as benchmarks_file:
    benchmarks_file_writer = csv.writer(benchmarks_file, delimiter=',')
    index = open('csv2/index.csv', 'r', encoding='utf-8')
    index_reader = csv.reader(index, delimiter=',')
    # skip header
    next(index_reader)
    header_written = False
    counter = 0
    for line in index_reader:
        current_csv = open(line[1], 'r', encoding='utf-8')
        current_csv_reader = csv.reader(current_csv, delimiter=',')
        if not header_written:
            benchmarks_file_writer.writerow(next(current_csv_reader))
            header_written = True
        else:
        # Get rid of csv header
            next(current_csv_reader)
        for row in current_csv_reader:
            funcname = row[1].split('/')[-1]
            if funcname.startswith('Benchmark'):
                benchmarks_file_writer.writerow(row)
        current_csv.close()
        counter += 1
        print(str(counter) + " project merged.")
