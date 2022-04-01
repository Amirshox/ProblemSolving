class Solution:
    def solve(self, s):
        result = ""
        for i in s:
            if i.isalpha() and i.islower():
                result += i
        return result == result[::-1]
