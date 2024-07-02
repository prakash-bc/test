package main

import (
	"fmt"
	"strings"
)

func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		for l < r && !isAlphaNumeric(int(s[l])) {
			l += 1
		}
		for l < r && !isAlphaNumeric(int(s[r])) {
			r -= 1
		}
		if strings.ToLower(string(s[l])) != strings.ToLower(string(s[r])) {
			return false

		}
		l += 1
		r -= 1

	}
	return true

}
func isAlphaNumeric(asciCode int) bool {
	return (int('a') <= asciCode && asciCode <= int('z') ||
		int('A') <= asciCode && asciCode <= int('Z') ||
		int('0') <= asciCode && asciCode <= int('9'))
}
func main() {
	fmt.Println(isPalindrome("race a car"))

}
