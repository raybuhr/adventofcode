package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	grid := Grid{
		Numbers: [][]string{{"1", "2", "3"}, {"4", "5", "6"}, {"7", "8", "9"}},
		NumCols: 3,
		NumRows: 3,
	}
	// file, err := os.Open("test_input.txt")
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()
	steps := [][]string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		instructions := strings.Split(scanner.Text(), "")
		steps = append(steps, instructions)
	}

	buttons := map[int]Button{}
	start := Button{
		Col: 1,
		Row: 1,
		Val: grid.Numbers[1][1],
	}

	for i, step := range steps {
		for _, letter := range step {
			start = move(letter, start, grid)
		}
		buttons[i] = start
	}

	fmt.Println("Part 1 Solution:")
	for j := 0; j < len(buttons); j++ {
		fmt.Println(buttons[j].Val)
	}

	grid2 := Grid{
		Numbers: [][]string{
			{"", "", "1", "", ""},
			{"", "2", "3", "4", ""},
			{"5", "6", "7", "8", "9"},
			{"", "A", "B", "C", ""},
			{"", "", "D", "", ""},
		},
		NumCols: 5,
		NumRows: 5,
	}
	start2 := Button{0, 1, "5"}
	buttons2 := map[int]Button{}
	for i, step := range steps {
		for _, letter := range step {
			start2 = move(letter, start2, grid2)
		}
		buttons2[i] = start2
	}

	fmt.Println("\nPart 2 Solution:")
	for k := 0; k < len(buttons2); k++ {
		fmt.Println(buttons2[k].Val)
	}
}

type Button struct {
	Col int
	Row int
	Val string
}

type Grid struct {
	Numbers [][]string
	NumCols int
	NumRows int
}

func move(step string, start Button, grid Grid) Button {
	newRow, newCol, newVal := start.Row, start.Col, start.Val
	if step == "U" {
		newRow = start.Row - 1
	}
	if step == "D" {
		newRow = start.Row + 1
	}
	if step == "L" {
		newCol = start.Col - 1
	}
	if step == "R" {
		newCol = start.Col + 1
	}

	if newRow >= 0 && newRow < grid.NumRows {
		if newCol >= 0 && newCol < grid.NumCols {
			newVal = grid.Numbers[newRow][newCol]
			if newVal != "" {
				newButton := Button{Row: newRow, Col: newCol, Val: newVal}
				return newButton
			}
		}
	}
	return start
}
