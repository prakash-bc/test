package main

import "fmt"

func topKFrequent(nums []int, k int) []int {
	bucket := map[int]int{}
	for _, n := range nums {
		bucket[n]++
	}

	freq := make([][]int, len(nums)+1)
	for k := range bucket {
		freq[k] = append(freq[k], bucket[k])

	}
	for n := len(bucket); n > 0; n -= 1 {
		for _, s := range freq[n] {
			fmt.Println(s, "DDDDDDDDDDDD")
		}
	}
	fmt.Println(freq, bucket)
	ans := []int{}
	return ans
}
func main() {
	topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2)
}
