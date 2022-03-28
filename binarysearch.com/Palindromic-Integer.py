class Solution:
    result = 0

    def solve(self, num):
        if num > 0:
            remainder = num % 10
            self.result = (self.result * 10) + remainder
            self.solve(num // 10)
        if num == self.result:
            return True
        else:
            return False
