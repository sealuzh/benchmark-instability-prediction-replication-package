package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"strings"

	"github.com/sealuzh/goabs/deps"
)

func main() {

	csvpath := os.Args[1]
	csvfile, _ := os.Open(csvpath)
	r := csv.NewReader(bufio.NewReader(csvfile))
	r.Comma = ';'
	lines, _ := r.ReadAll()
	errs := 0
	getCmd := exec.Command("go", "get", "-t", "./...")

	for count, line := range lines {
		githubName := line[0]
		fmt.Println(githubName)
		projectPath := line[2]

		gopath := strings.Split(line[2], string(os.PathSeparator)+"src")[0]
		os.Setenv("GOPATH", gopath)

		getCmd.Dir = projectPath
		getCmd.Env = os.Environ()
		getCmd.Output()

		err := deps.Fetch(projectPath, "")
		if err != nil {
			fmt.Println(err)
			errs++
		}

		fmt.Println(strconv.Itoa(count+1) + " projects' dependencies fetched.")

	}
	fmt.Println(strconv.Itoa(errs) + " projects gave an error while fetching dependencies.")
}
