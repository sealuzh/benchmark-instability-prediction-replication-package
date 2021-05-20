import pandas as pd
import csv

df_csv1 = pd.read_csv('csv1.csv', delimiter=',')
df_csv2 = pd.read_csv('benchmark_properties.csv', delimiter=',')

df = pd.concat([df_csv1, df_csv2])
df = df.reset_index(drop=True)

duplicateRowsDF = df[df.duplicated()]

for row in duplicateRowsDF.iterrows():
    print(row[1].project_name, row[1].function)
duplicated_list = [row[1].project_name+row[1].function for row in duplicateRowsDF.iterrows()]
# print(duplicated_list)
print(len(duplicated_list))

csv1Dict = {}
csv1Header = ''
with open('csv1.csv', 'r') as benchfile:
    reader = csv.reader(benchfile, delimiter=',')
    # skip header
    csv1Header = next(reader)
    for row in reader:
        id = row[0]+row[1]
        csv1Dict[id] = row

# This codeblock is to create benchmark_properties_valid by removing 121 equal rows found in both csv1 and csv2
benchmark_properties_valid = open('benchmark_properties_valid.csv', 'w', encoding='utf-8', newline='')
newwriter = csv.writer(benchmark_properties_valid)
csvFeaturesIdx = 3

with open('benchmark_properties.csv', 'r', encoding='utf-8') as benchfile:
    old_reader = csv.reader(benchfile, delimiter=',')
    
    # new header
    csv2Header = next(old_reader)
    newHeader = csv2Header[:csvFeaturesIdx]
    newHeader.extend(['code_'+fn for fn in csv2Header[csvFeaturesIdx:]])
    newHeader.extend(['bench_'+fn for fn in csv1Header[csvFeaturesIdx:]])

    newwriter.writerow(newHeader)

    for row in old_reader:
        id = row[0]+row[1]
        if id not in duplicated_list:
            newrow = row.copy()
            benchOnlyRow = csv1Dict[id]
            newrow.extend(benchOnlyRow[csvFeaturesIdx:])
            newwriter.writerow(newrow)
