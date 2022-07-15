# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025


class Solution:
    def solve(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.solve(n - 1) + self.solve(n - 2)


s = Solution()
print(s.solve(22))
