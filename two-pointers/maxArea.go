package main

import "fmt"

func maxArea(h []int) int {
	l, r := 0, len(h)-1
	res := 0
	for l < r {
		minH := min(h[l], h[r])
		res = max(res, (r-l)*minH)
		if h[l] < h[r] {
			l++
		} else {
			r -= 1
		}
	}
	fmt.Println(res, "RES")
	return res

}
func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func main() {
	maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7})

}
