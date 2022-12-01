package main

import (
	"fmt"
	utils "raybuhr/aoc/utils"
	"strconv"
	"strings"
)

func main() {
	var part1 int
	var part2 int
	data := utils.ReadLines("data.txt")
	part1 = moveTwoD(data)
	part2 = moveAndAim(data)
	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

func moveTwoD(data []string) int {
	position := 0
	depth := 0
	for _, line := range data {
		step := strings.Split(line, " ")
		cmd := step[0]
		amt, _ := strconv.Atoi(step[1])
		switch {
		case cmd == "forward":
			position += amt
		case cmd == "down":
			depth += amt
		case cmd == "up":
			depth -= amt
		}
	}
	return position * depth
}

func moveAndAim(data []string) int {
	position := 0
	depth := 0
	aim := 0

	for _, line := range data {
		step := strings.Split(line, " ")
		cmd := step[0]
		amt, _ := strconv.Atoi(step[1])
		switch {
		case cmd == "forward":
			position += amt
			depth += aim * amt
		case cmd == "down":
			aim += amt
		case cmd == "up":
			aim -= amt
		}
	}
	return position * depth
}
