package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	openFile, err := os.Open("day7.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer openFile.Close()

	towers := []Tower{}
	rawLines := bufio.NewScanner(openFile)
	for rawLines.Scan() {
		rawText := rawLines.Text()
		rawText = strings.Replace(rawText, "(", "", -1)
		rawText = strings.Replace(rawText, ")", "", -1)
		rawText = strings.Replace(rawText, "->", "", -1)
		words := strings.Fields(rawText)
		weight, err := strconv.Atoi(words[1])
		if err != nil {
			fmt.Println(err)
		}
		tower := Tower{
			Name:   words[0],
			Weight: weight,
		}
		children := []string{}
		if len(words) > 2 {
			for i, word := range words {
				if i < 2 {
					continue
				} else {
					children = append(children, word)
				}
			}
			tower.Children = children
		}
		towers = append(towers, tower)
	}

	for i, t := range towers {
		fmt.Println(i, ":", t)
	}
}

type Tower struct {
	Name     string
	Weight   int
	Children []string
}
