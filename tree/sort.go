package main

import "fmt"

func main() {
	nums := []int{4, 7, 1, 2, 5, 3}
	// fmt.Println(selectionSort(nums))
	fmt.Println(mergeSort(nums))
	// // selectionSort(nums)
}

func bubbleSort(nums []int) []int {
	n := len(nums)
	for i := n - 1; i > 0; i -= 1 {
		fmt.Println(nums[i])
		for j := 0; j < i; j += 1 {
			fmt.Println(nums[j], "DDD")
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
	return nums
}

func insertionSort(nums []int) []int {
	n := len(nums)
	for i := 0; i < n; i += 1 {
		fmt.Println(nums[i])
		j := i
		for j > 0 {
			if nums[j-1] > nums[j] {
				nums[j], nums[j-1] = nums[j-1], nums[j]
			}
			j -= 1
		}
	}
	return nums
}

func selectionSort(nums []int) []int {
	n := len(nums)
	for i := 0; i < n; i += 1 {
		min := i
		for j := i; j < n; j += 1 {
			if nums[j] < nums[min] {
				min = j
			}
		}
		nums[i], nums[min] = nums[min], nums[i]
	}
	return nums
}

func mergeSort(nums []int) []int {
	n := len(nums)
	if n <= 1 {
		return nums
	}
	l, r := mergeSort(nums[:n/2]), mergeSort(nums[n/2:])
	return merge(l, r)
}

func merge(a, b []int) []int {
	final := make([]int, 0, len(a)+len(b))
	i, j := 0, 0
	for i < len(a) && j < len(b) {
		if a[i] < b[j] {
			final = append(final, a[i])
			i += 1
		} else {
			final = append(final, b[j])
			j += 1
		}
	}
	final = append(final, a[i:]...)
	final = append(final, b[j:]...)
	return final
}
