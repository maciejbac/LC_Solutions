package main

import "fmt"

// Test main method to feed input and print outupt of my solution function
func main() {

	// Call my function with test values
	var res = twoSum([]int{2, 7, 11, 15}, 9)

	// Display the results
	fmt.Println(res)
}

// Solution to the leetcode problem
// Dummy function for now
func twoSum(nums []int, target int) []int {

	var table = []int{0, 1}

	return table
}
