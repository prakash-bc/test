package main

import "fmt"

func makeSmallestPalindrome(s string) string {
	var res = []byte(s)
	left, right := 0, len(s)-1
	for left <= right {
		if int(s[left]) < int(s[right]) {
			res[right] = s[left]
		} else if int(s[left]) > int(s[right]) {
			res[left] = s[right]

		}
		left += 1
		right -= 1

	}
	fmt.Println(string(res), res)
	return s

}
func main() {
	makeSmallestPalindrome("egcfe")
}
