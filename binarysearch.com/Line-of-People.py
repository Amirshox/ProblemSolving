class Solution:
    def solve(self, n, a, b):
        return n - a if n - a <= b else b + 1


s = Solution()
print(s.solve(10, 3, 4))
