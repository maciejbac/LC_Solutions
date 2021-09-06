package main

import "fmt"

// Test main method to feed input and print outupt of my solution function
func main() {

	// Call my function with test values
	var res = twoSum([]int{1, 3, 5, 8, 9}, 10)

	// Display the results
	fmt.Println(res)
}

// Solution to the leetcode problem
// Dummy function for now
func twoSum(nums []int, target int) []int {

	// Declare a new map of integers
	numsMap := make(map[int]int)

	for i, num := range nums {

		if idx, ok := numsMap[target-num]; ok {
			return []int{idx, i}
		}

		numsMap[num] = i
	}

	return []int{0, 0}
}
