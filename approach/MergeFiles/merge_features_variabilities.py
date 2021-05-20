import pandas as pd
import csv
import sys

# run with 5, 10, 20, 30
nr_iterations = int(sys.argv[1])

final_name = "final_{}_iterations.csv".format(nr_iterations)
df_var = pd.read_csv(final_name, delimiter=',')
df_prop_valid = pd.read_csv('benchmark_properties_valid.csv', delimiter=',')

# Having only project_name, function and rciw99 of final.csv
# df_var = df_var.drop(['executions', 'mean', 'cv', 'rciw95'], axis=1)

# Dropping
df_prop_valid = df_prop_valid.drop(['id'], axis=1)

# Join them on project_name & function
df_merged_valid = pd.merge(df_var, df_prop_valid, on=['project_name', 'function'])
merged_name = "merged_valid_{}_iterations.csv".format(nr_iterations)
df_merged_valid.to_csv(merged_name, index=False)
