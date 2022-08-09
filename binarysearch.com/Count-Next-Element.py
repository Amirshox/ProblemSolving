class Solution:
    def solve(self, nums):
        set_nums = set(nums)
        count = 0
        for x in nums:
            if x + 1 in set_nums:
                count += 1
        return count
