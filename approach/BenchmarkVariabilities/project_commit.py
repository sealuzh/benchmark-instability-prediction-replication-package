# Just to get projects and their commit to pull them from Github via the other py file

import csv

newfile = open("project_commit.csv", 'w', encoding='utf-8', newline='')
writer = csv.writer(newfile, delimiter=';')

with open("pa_input_projects.csv", 'r') as projects:
    for line in projects:
        path = line.rstrip()
        project = open(path, 'r', encoding='utf-8')
        project.readline()
        reader = csv.reader(project, delimiter=';')
        for row in reader:
            writer.writerow([row[0],row[1]])
            break



