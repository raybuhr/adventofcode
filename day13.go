package main

import (
	"fmt"
	"reflect"
)

func main() {
	depths := map[int]int{
		0:  3,
		1:  2,
		2:  4,
		4:  4,
		6:  5,
		8:  8,
		10: 6,
		12: 6,
		14: 6,
		16: 6,
		18: 8,
		20: 8,
		22: 12,
		24: 10,
		26: 9,
		28: 8,
		30: 8,
		32: 12,
		34: 12,
		36: 12,
		38: 12,
		40: 8,
		42: 12,
		44: 14,
		48: 10,
		46: 14,
		50: 12,
		52: 12,
		54: 14,
		56: 14,
		58: 14,
		62: 12,
		64: 14,
		66: 14,
		68: 14,
		70: 12,
		74: 14,
		76: 14,
		78: 14,
		80: 18,
		82: 17,
		84: 30,
		88: 14,
	}

	winner := map[string]int{}
	// for delay := 0; delay <= 5000000; delay++ {
	// correct answer was 3960702
	for delay := 3960702; delay <= 3960702; delay++ {
		positions := []int{}
		for d, r := range depths {
			pos := get_node_current_position(r, d+delay)
			positions = append(positions, pos)
		}
		if HasElem(positions, 0) == false {
			winner["delay"] = delay
		}
	}
	fmt.Println(winner)
	for d, r := range depths {
		fmt.Println(
			"Depth:",
			d,
			", Range:", r,
			// ", Delay:", winner["delay"],
			", Position:",
			get_node_current_position(r, (d+winner["delay"])),
		)
	}

	// A little QA
	fmt.Println(get_node_current_position(2, 1+3999997) == 0)
}

func HasElem(s interface{}, elem interface{}) bool {
	arrV := reflect.ValueOf(s)

	if arrV.Kind() == reflect.Slice {
		for i := 0; i < arrV.Len(); i++ {

			// XXX - panics if slice element points to an unexported struct field
			// see https://golang.org/pkg/reflect/#Value.Interface
			if arrV.Index(i).Interface() == elem {
				return true
			}
		}
	}

	return false
}

func get_node_current_position(node_range, seconds int) int {
	list_node_range := []int{}
	for i := 0; i <= node_range; i++ {
		list_node_range = append(list_node_range, i)
	}
	for j := (node_range - 1); j > 0; j-- {
		list_node_range = append(list_node_range, j)
	}
	idx := seconds % len(list_node_range)
	pos := list_node_range[idx]
	fmt.Println(list_node_range)
	fmt.Println(idx)
	return pos
}

// Working in Python
// def get_node_current_position(node_range, seconds):
//     list_node_range = list(range(node_range))
// 	   cycle_list = list_node_range + list_node_range[-2:0:-1]
// 	   if seconds >= len(cycle_list):
//         idx = seconds % len(cycle_list)
//         pos = cycle_list[idx]
// 	   else:
//         pos = cycle_list[seconds]
//     return pos
