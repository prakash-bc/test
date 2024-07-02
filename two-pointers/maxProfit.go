package main

import "fmt"

func maxProfit(prices []int) int {
	fmt.Println(prices)
	l, r := 0, 1
	n := len(prices)
	res := 0
	for r < n {
		diff := prices[r] - prices[l]
		res = max(diff, res)
		if diff < 0 {
			l += 1
		}
		r += 1

	}
	fmt.Println(res)
	return res
}
func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
func main() {
	maxProfit([]int{7, 1, 5, 3, 6, 4})

}
