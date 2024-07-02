package main

import "fmt"

func longestConsecutive(nums []int) int {

	maxLen := 0
	set := map[int]bool{}
	for _, num := range nums {
		set[num] = true
	}
	for n := range set {
		if _, ok := set[n-1]; !ok {
			cLen := 1
			for {
				if _, ok := set[n+cLen]; ok {
					cLen += 1
					continue
				}
				if cLen > maxLen {
					maxLen = cLen
				}
				break

			}
		}

	}
	fmt.Println(maxLen)
	return maxLen
}
func main() {
	longestConsecutive([]int{100, 4, 200, 1, 3, 2})
}
