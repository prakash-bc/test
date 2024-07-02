package main

import "fmt"

func findDuplicate(nums []int) int {
	slow, fast := 0, 0
	for true {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast {
			break
		}

	}
	slow2 := 0
	for true {
		slow = nums[slow]
		slow2 = nums[slow2]
		if slow == slow2 {
			return slow
		}

	}
	fmt.Println(slow)
	return -1

}
func main() {
	findDuplicate([]int{1, 3, 4, 2, 2})

}

// Input: nums = [1,3,4,2,2]
// Output: 2
