package main

import "fmt"

func minEatingSpeed(piles []int, h int) int {
	max := 0
	for _, p := range piles {
		if p > max {
			max = p
		}
	}
	left, right := 1, max
	res := max
	fmt.Println(left, right, res)

	for left <= right {
		speed := (left + right) / 2
		totalTime := (0)
		for _, p := range piles {
			totalTime += (p) / (speed)
			if (p)%(speed) != 0 {
				totalTime += 1
			}
		}
		if totalTime <= h {
			res = speed
			right = speed - 1
		} else {
			left = speed + 1

		}
		fmt.Println(totalTime)
	}
	fmt.Println(res, "EEEE")
	return res
}

func main() {

	piles := []int{3, 6, 7, 11}
	h := 8
	fmt.Println(minEatingSpeed(piles, h))

}
