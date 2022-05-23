class Solution:
    def solve(self, nums):
        count = 0
        flipping = False
        for i in range(len(nums)):
            if nums[i] == 1:
                flipping = True
            if flipping and (i == 0 or nums[i] != nums[i - 1]):
                count += 1
        return count
