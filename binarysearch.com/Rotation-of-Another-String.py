class Solution:
    def solve(self, s0, s1):
        return (len(s0) == len(s1)) & (s0 in s1 + s1)


s = Solution()
print(s.solve("abc", "cab"))
