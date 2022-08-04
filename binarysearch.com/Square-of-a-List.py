class Solution:
    def solve(self, nums):
        return sorted([num ** 2 for num in nums])


s = Solution()
print(s.solve([-5, -3, 0, 1, 4]))
