package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/sealuzh/sscf/pkg"
	"gonum.org/v1/gonum/graph/simple"
)

func main() {
	csvfile, _ := os.Open("csv1/index.csv")
	r := csv.NewReader(bufio.NewReader(csvfile))
	r.Comma = ','
	// Get rid of header
	r.Read()
	// Get all the projects
	lines, _ := r.ReadAll()

	if _, err := os.Stat("csv2"); os.IsNotExist(err) {
		os.Mkdir("csv2", os.ModePerm)
	}

	indexName := "csv2" + string(os.PathSeparator) + "index.csv"
	var indexFile *os.File
	var indexWriter *csv.Writer
	if _, err := os.Stat(indexName); err == nil {
		indexFile, _ = os.OpenFile(indexName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		indexWriter = csv.NewWriter(indexFile)
	} else {
		indexFile, _ = os.Create(indexName)
		indexWriter = csv.NewWriter(indexFile)
		indexWriter.Write([]string{"name", "csvpath"})
		indexWriter.Flush()
	}

	// Start main loop
	for count, line := range lines {
		// Reading all functions
		projectCSVPath := line[1]
		projectCSVFile, _ := os.Open(projectCSVPath)
		f := csv.NewReader(bufio.NewReader(projectCSVFile))
		f.Comma = ','
		// Get rid of header
		f.Read()
		functions, _ := f.ReadAll()

		// Setup for the output folder
		projectName := line[0]
		nnProjectName := strings.Replace(projectName, "/", "&", -1)
		outputName := "csv2" + string(os.PathSeparator) + strconv.Itoa(count+1) + "&" + nnProjectName + ".csv"
		if _, err := os.Stat(outputName); err == nil {
			continue
		}

		// Getting benchmarks from csv file
		var benchmarks [][]string
		for _, function := range functions {
			if strings.Contains(function[1], "Benchmark") {
				benchmarks = append(benchmarks, function)
			}
		}

		projectPath := line[2]
		callgraph := simple.NewDirectedGraph()
		nodemap := make(pkg.NodeMap)

		pkg.WalkPathCG(projectPath, callgraph, nodemap)

		var records [][]string

		// Iterating each Benchmark
		for _, benchmark := range benchmarks {
			reachables := make(pkg.ReachableNodes)
			benchmarkNode := nodemap[benchmark[1]]

			// If this benchmark wasn't a part of callgraph result, skip this benchmark
			if benchmarkNode == nil {
				continue
			}

			// Collecting reachable nodes for the benchmark, in form of CSV1 Entries
			pkg.FromNext(callgraph, benchmarkNode, reachables)

			var reachablesCSV [][]string

			for node := range reachables {
				funcID := pkg.NodeLookUp(node, nodemap)
				if funcID != "" {
					// Search for the function in csv1
					for _, function := range functions {
						if funcID == function[1] {
							reachablesCSV = append(reachablesCSV, function)
							break
						}
					}
				}
			}

			newvaluesmap := make(map[int]int)
			for _, function := range reachablesCSV {
				for i := 2; i < len(function); i++ {
					numval, _ := strconv.Atoi(function[i])
					newvaluesmap[i] += numval
				}
			}
			records = append(records, pkg.SumToRecord(projectName, newvaluesmap, benchmark))
		}
		pkg.WriteCSV2(outputName, records)
		indexWriter.Write([]string{projectName, outputName})
		indexWriter.Flush()

		fmt.Println("Completed projects:" + strconv.Itoa(count+1))
	}
}
