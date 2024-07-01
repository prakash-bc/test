package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	stack := []int{}
	ops := map[string]func(a, b int) int{
		"+": func(a, b int) int { return a + b },
		"-": func(a, b int) int { return b - a },
		"*": func(a, b int) int { return a * b },
		"/": func(a, b int) int { return b / a },
	}
	for _, token := range tokens {
		op, ok := ops[token]
		if ok {
			a, b := stack[len(stack)-1], stack[len(stack)-2]
			res := op(a, b)
			fmt.Println(a, b, res, token, 13/5)
			stack = append(stack[:len(stack)-2], res)
			continue
		}
		n, _ := strconv.Atoi(token)
		stack = append(stack, n)

	}
	fmt.Println(stack)
	return 1
}
func main() {

	evalRPN([]string{"4", "13", "5", "/", "+"})

}
