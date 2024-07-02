package main

func checkInclusion(s1 string, s2 string) bool {
	n, m := len(s1), len(s2)
	if n > m {
		return false
	}

	s1Count := [26]int{}
	for i := 0; i < n; i++ {
		s1Count[s1[i]-'a'] += 1
	}
	s2Count := [26]int{}
	for i := 0; i < n-1; i++ {
		s2Count[s2[i]-'a'] += 1
	}
	if s1Count == s2Count {
		return true
	}

	for i := n - 1; i < m; i++ {
		s2Count[s2[i]-'a'] += 1

		if s1Count == s2Count {
			return true
		}
		s2Count[s2[i-n+1]-'a'] -= 1
	}
	return false
}
func main() {
	s1 := "ab"
	s2 := "ab"
	checkInclusion(s1, s2)
}
