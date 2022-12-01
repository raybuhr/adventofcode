package utils

import (
	"io/ioutil"
	"strings"
)

func ReadFile(path string) string {
	content, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}

	strContent := string(content)
	return strings.TrimRight(strContent, "\n")
}

func ReadLines(path string) []string {
	lines := []string{}
	data := ReadFile(path)
	for _, line := range strings.Split(data, "\n") {
		lines = append(lines, line)
	}
	return lines
}
