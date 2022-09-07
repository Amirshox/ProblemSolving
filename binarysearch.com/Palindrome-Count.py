class Solution:
    def solve(self, s, k):
        N = len(set(s))

        return N ** (k // 2 + k % 2)


s = Solution()
print(s.solve('abc', 4))
