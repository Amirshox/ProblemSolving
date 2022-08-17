class Solution:
    def solve(self, nums):
        nums.sort()
        max_difference = 0
        for i in range(1, len(nums)):
            difference = nums[i] - nums[i - 1]
            if max_difference < difference:
                max_difference = difference
        return max_difference


s = Solution()
print(s.solve(nums=[4, 1, 2, 8, 9, 10]))
