package main

import (
	"fmt"
	utils "raybuhr/aoc/utils"
	"strconv"
	"strings"
)

func main() {
	data := utils.ReadFile("data.txt")
	var part1 int
	var part2 int

	part1 = countIncreases(data)
	fmt.Println("Part 1:", part1)

	part2 = countRollingThrees(data)
	fmt.Println("Part 2:", part2)
}

func countIncreases(data string) int {
	nums := parseData(data)
	ct := 0
	for i, num := range nums {
		if i > 0 {
			if num > nums[i-1] {
				ct++
			}
		}
	}
	return ct
}

func countRollingThrees(data string) int {
	nums := parseData(data)
	ct := 0
	for i, num := range nums {
		if i > 2 {
			current := num + nums[i-1] + nums[i-2]
			prev := current - num + nums[i-3]
			if current > prev {
				ct++
			}
		}
	}
	return ct
}

func parseData(data string) []int {
	nums := []int{}
	for _, line := range strings.Split(data, "\n") {
		num, _ := strconv.Atoi(line)
		nums = append(nums, num)
	}
	return nums
}
