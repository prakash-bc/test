package main

import "fmt"

func search(nums []int, target int) int {

	n := len(nums)
	fmt.Println(n)
	l := 0
	r := n - 1
	for l < r {
		mid := l + (r-l)/2
		if target < nums[mid] {
			r = mid - 1
		} else if target > nums[mid] {
			l = mid + 1
		} else {
			return mid
		}

	}

	return -1

}

// Input: nums = [-1,0,3,5,9,12], target = 9
// Output: 4
func main() {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 9
	fmt.Println(search(nums, target))
}
