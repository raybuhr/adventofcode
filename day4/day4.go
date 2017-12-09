package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	inputFile, err := os.Open("day4.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer inputFile.Close()

	filelines := []string{}
	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		text := scanner.Text()
		filelines = append(filelines, text)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	validLines := 0
	for _, line := range filelines {
		words := strings.Split(line, " ")

		if len(words) == len(uniqueWordCount) {
			validLines = validLines + 1
		}
		fmt.Printf("Words: %d, Unique: %d  |  %v\n", len(words), len(uniqueWordCount), line)
	}

	fmt.Println(validLines)
}

func dedupWords(words []string) []string {
	uniqueWords := map[string]bool{}
	uniqueWordCount := []string{}
	for w := range words {
		if uniqueWords[words[w]] == true {
			continue
		} else {
			uniqueWordCount = append(uniqueWordCount, words[w])
		}
	}
	return uniqueWordCount
}
