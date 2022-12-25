package main

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func longestPalindrome(s string) string {
	max_len := 0
	max_str := ""
	for i := 0; i < len(s); i++ {
		for j := i + 1; j <= len(s); j++ {
			if isPalindrome(s[i:j]) {
				if j-i > max_len {
					max_len = j - i
					max_str = s[i:j]
				}
			}
		}
	}
	return max_str
}

func main() {
	println(longestPalindrome("babad"))
	println(longestPalindrome("cbbd"))
	println(longestPalindrome("a"))
	println(longestPalindrome("ac"))
}
