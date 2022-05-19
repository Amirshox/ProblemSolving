class Solution:
    def solve(self, s):
        result = s[0]
        for ch in s:
            if ch == result[-1]:
                continue
            else:
                result += ch
        return result
