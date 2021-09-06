package main

import "fmt"

// Test main method to feed input and print outupt of my solution function
func main() {

	// Call my function with test values
	var res = twoSum([]int{0, 1, 3, 5, 8, 9}, 10)

	// Display the results
	fmt.Println(res)
}

// Solution to the leetcode problem
// Dummy function for now
func twoSum(nums []int, target int) []int {

	// Nested for loop to iterate through the array twice and compare the numbers if they are a match
	for i := 0; i < len(nums); i++ {
		// Advance the iterator by 1 to avoid comparing a number to itself
		for j := i + 1; j < len(nums); j++ {
			// If a match is found, return an array that contains the indexes of the found numbers
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return nil
}
