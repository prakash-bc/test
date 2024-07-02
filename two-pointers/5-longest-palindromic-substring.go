package main

import "fmt"

func longestPalindrome(s string) string {
	resLen := 0
	res := ""
	for i := 0; i < len(s); i++ {
		l, r := i, i
		for l > 0 && r < len(s) && s[l] == s[r] {
			tempLen := r - l + 1
			if tempLen > resLen {
				res = s[l : r+1]
				resLen = tempLen
			}
			l -= 1
			r += 1
		}

	}
	fmt.Println(res)
	return res

}

func main() {
	longestPalindrome("babad")
}
