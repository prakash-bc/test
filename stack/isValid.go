package main

import "fmt"

func isValid(s string) bool {
	pairs := map[rune]rune{
		'}': '{',
		']': '[',
		')': '(',
	}
	stack := make([]rune, 0)
	fmt.Println(stack, pairs)
	for _, item := range s {
		// fmt.Println("SSS", item)
		// fmt.Printf("%#T\n", item)
		pair, ok := pairs[item]
		if !ok {
			stack = append(stack, item)
			continue
		}
		if len(stack) == 0 {
			return false
		}
		if stack[len(stack)-1] != pair {
			return false
		}
		stack = stack[:len(stack)-1]
		// fmt.Println(stack, stack[len(stack)-1], pair)
		// if len(stack)==0 || stack[-1]!= pairs[item]

	}
	return len(stack) == 0
}
func main() {

	fmt.Println(isValid("()[]{}"))
}
