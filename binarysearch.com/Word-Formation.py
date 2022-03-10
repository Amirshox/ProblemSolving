class Solution:
    def solve(self, words, letters):
        max_length = 0
        for word in words:
            answer = False
            new_letters = list(letters)
            for ch in word:
                if ch in new_letters:
                    answer = True
                    new_letters.remove(ch)
                else:
                    answer = False
                    break
            if answer and max_length < len(word):
                max_length = len(word)
        return max_length
