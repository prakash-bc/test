package main

import "fmt"

func searchRange(nums []int, target int) []int {
	left := searchBS(nums, target, true)
	right := searchBS(nums, target, false)
	return []int{left, right}

}
func searchBS(nums []int, target int, lb bool) int {
	result := -1
	left, right := 0, len(nums)-1
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			result = mid
			if lb {
				right = mid - 1
			} else {
				left = mid + 1
			}

		} else if target < nums[mid] {
			right = mid - 1
		} else {
			left = mid + 1
		}

	}

	return result
}

func main() {
	nums := []int{5, 7, 7, 8, 8, 10}
	target := 8
	fmt.Println(searchRange(nums, target))
}
