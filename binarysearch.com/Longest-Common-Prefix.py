class Solution:
    def solve(self, words):
        min_word = min(words, key=len, default="")
        for end in range(len(min_word), -1, -1):
            if all(word.startswith(min_word[:end]) for word in words):
                return min_word[:end]
        return ""
