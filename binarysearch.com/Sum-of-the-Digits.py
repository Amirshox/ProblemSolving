class Solution:
    def solve(self, num):
        result = 0
        for digit in str(num):
            result += int(digit)
        return result
