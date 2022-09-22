package main

func IsTriangle(a, b, c int) bool {
	if a <= 0 && b <= 0 && c <= 0 {
		return false
	} else {
		if a+b <= c {
			return false
		} else if a+c <= b {
			return false
		} else if b+c <= a {
			return false
		} else {
			return true
		}
	}
}
