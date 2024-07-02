package main

import "fmt"

func groupAnagrams(strs []string) [][]string {
	res := [][]string{}
	m := map[[26]int][]string{}

	for _, str := range strs {
		t := [26]int{}
		for _, s := range str {
			t[s-'a'] += 1
		}
		m[t] = append(m[t], str)

		fmt.Println(t, str)
	}
	for _, val := range m {
		res = append(res, val)

	}
	return res
}
func main() {
	groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"})

}
