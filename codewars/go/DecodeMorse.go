package main

import (
	"strings"
)

func DecodeMorse(morseCode string) (decoded string) {
	MorseCode := map[string]string{
		".-":   "A",
		"-...": "B",
		"-.-.": "C",
		"-..":  "D",
		".":    "E",
		"..-.": "F",
		"--.":  "G",
		"....": "H",
		"..":   "I",
		".---": "J",
		"-.-":  "K",
		".-..": "L",
		"--":   "M",
		"-.":   "N",
		"---":  "O",
		".--.": "P",
		"--.-": "Q",
		".-.":  "R",
		"...":  "S",
		"-":    "T",
		"..-":  "U",
		"...-": "V",
		".--":  "W",
		"-..-": "X",
		"-.--": "Y",
		"--..": "Z",
	}
	for _, word := range strings.Split(strings.TrimSpace(morseCode), "   ") {
		for _, char := range strings.Split(word, " ") {
			decoded += MorseCode[char]
		}
		decoded += " "
	}
	return strings.TrimSpace(decoded)
}
