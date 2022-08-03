class Solution:
    def solve(self, n):
        empty = 0
        drunken = 0

        while n:
            drunken += n
            empty += n
            n = empty // 3
            empty %= 3

        return drunken


s = Solution()
print(s.solve(761))
