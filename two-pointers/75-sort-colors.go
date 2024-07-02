package main

func sortColors(nums []int) {
	l, r := 0, len(nums)-1
	i := 0
	for i <= r {
		if nums[i] == 0 {
			nums[l], nums[i] = nums[i], nums[l]
			i++
			l++

		} else if nums[i] == 1 {
			i++

		} else {
			nums[r], nums[i] = nums[i], nums[r]
			r--
		}
	}
}
func main() {

	sortColors([]int{2, 0, 2, 1, 1, 0})
}
