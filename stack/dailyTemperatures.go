package main

func dailyTemperatures(temperatures []int) []int {
	res := make([]int, len(temperatures))
	stack := make([][]int, 0)
	for index, item := range temperatures {
		for len(stack) != 0 && stack[len(stack)-1][0] < item {
			_, si := stack[len(stack)-1][0], stack[len(stack)-1][1]
			res[si] = index - si
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, []int{item, index})

	}
	return res
}
func main() {
	dailyTemperatures([]int{73, 74, 75, 71, 69, 72, 76, 73})
}
