package main

import "fmt"

func searchMatrix(matrix [][]int, target int) bool {
	rows, cols := len(matrix), len(matrix[0])
	left, right := 0, rows*cols-1
	for left <= right {
		mid := (left + right) / 2
		r, c := mid/cols, mid%cols
		fmt.Println("m", mid, r, c)
		if matrix[r][c] == target {
			return true
		} else if matrix[r][c] < target {
			left = mid + 1

		} else {
			right = mid - 1

		}
	}
	return false
}
func main() {
	matrix := [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}
	target := 3
	fmt.Println(searchMatrix(matrix, target))

	// # Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
	// # Output: true
	// matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
	// target = 3

}
