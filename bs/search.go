package main

import "fmt"

// https://leetcode.com/problems/search-in-rotated-sorted-array/description/
func Bsearch(nums []int, target int) int {

	left, right := 0, len(nums)
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			return mid
		} else if target <= nums[mid] {
			right = mid - 1

		} else {
			left = mid + 1
		}

	}
	return -1

}
func search(nums []int, target int) int {
	left, right := 0, len(nums)-1

	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			return mid
		} else if nums[left] <= nums[mid] {
			if target > nums[mid] || target < nums[left] {
				left = mid + 1
			} else {
				right = mid - 1
			}

		} else {
			if target < nums[mid] || target > nums[right] {
				right = mid - 1
			} else {

				left = mid + 1

			}

		}

	}
	return -1
}

func main() {
	// nums = [4,5,6,7,0,1,2], target = 0
	// fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 0))

}
