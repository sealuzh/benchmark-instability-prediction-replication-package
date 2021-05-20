# Downloads projects from Github

import subprocess, csv, os, sys

# Give here the folder to download the projects into
download_folder = sys.argv[1]

newfile = open('project_commit_place.csv', 'w', encoding='utf-8', newline='')

with open("project_commit.csv", 'r', encoding='utf-8') as store:
    reader = csv.reader(store, delimiter=';')
    writer = csv.writer(newfile, delimiter=';')
    counter = 0
    failed_projects = []

    for line in reader:
        counter += 1
        splitted = line[0].split('/')
        name = splitted[0]
        project = splitted[1]
        commit = line[1]
        new_folder = download_folder + os.sep + name + os.sep + project
        errors = 0

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            os.environ['GOPATH'] = new_folder
            url = f"github.com/{name}/{project}"
            print(url)

            try:
                get = subprocess.run(['go', 'get', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                errors += 1
                print(f"Failed to go get {url}")

            project_folder = new_folder + os.sep + 'src' + os.sep + url.replace('/', os.sep)
            try:
                changecommit = subprocess.run(['git', 'checkout', commit], cwd=project_folder, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                print(e.output)
                print(f"Failed to checkout to {commit} on {url}")
            except NotADirectoryError as n:
                print(n)
                print("This directory doesn't exits: " + project_folder)
                failed_projects.append(url)
            except FileNotFoundError as f:
                print(f)
                failed_projects.append(url)
            else:
                writer.writerow([line[0], line[1], project_folder])
                print(counter)

    print("Failed projects: ")
    print(failed_projects)
