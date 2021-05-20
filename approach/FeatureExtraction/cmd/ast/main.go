package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/sealuzh/sscf/pkg"
)

func main() {
	csvpath := os.Args[1]
	csvfile, _ := os.Open(csvpath)
	r := csv.NewReader(bufio.NewReader(csvfile))
	r.Comma = ';'
	lines, _ := r.ReadAll()

	if _, err := os.Stat("csv1"); os.IsNotExist(err) {
		os.Mkdir("csv1", os.ModePerm)
	}

	indexName := "csv1" + string(os.PathSeparator) + "index.csv"
	var indexFile *os.File
	var indexWriter *csv.Writer
	if _, err := os.Stat(indexName); err == nil {
		indexFile, _ = os.OpenFile(indexName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		indexWriter = csv.NewWriter(indexFile)
		indexWriter.Comma = ','
	} else {
		indexFile, _ = os.Create(indexName)
		indexWriter = csv.NewWriter(indexFile)
		indexWriter.Comma = ','
		indexWriter.Write([]string{"name", "csvpath", "projectpath"})
		indexWriter.Flush()
	}
	// Main loop of the program, iterates through all the project folders and creates csv files for each project, representing function properties in each line.
	for count, line := range lines {

		projectName := line[0]
		nnProjectName := strings.Replace(projectName, "/", "&", -1)
		projectPath := line[2]
		outputName := "csv1" + string(os.PathSeparator) + strconv.Itoa(count+1) + "&" + nnProjectName + ".csv"

		if _, err := os.Stat(outputName); err == nil {
			continue
		}

		gopath := strings.Split(line[2], string(os.PathSeparator)+"src")[0]
		os.Setenv("GOPATH", gopath)

		functions := make(pkg.FunctionMap)

		pkg.WalkPath(projectPath, functions)
		var records [][]string

		for f, fprop := range functions {
			records = append(records, pkg.FuncToRecord(projectName, f, fprop))
		}

		//// Print size of function pool of a project
		fmt.Println(len(records))

		pkg.WriteCSV(outputName, records)
		fmt.Println(count + 1)

		pkg.WriteIndexCsv(indexWriter, projectName, outputName, projectPath)

	}

}
