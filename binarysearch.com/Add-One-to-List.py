class Solution:
    def solve(self, nums):
        i = len(nums) - 1
        while i >= 0:
            if nums[i] + 1 <= 9:
                nums[i] = nums[i] + 1
                break
            else:
                nums[i] = 0
            i -= 1
        if i < 0:
            nums.insert(0, 1)
        return nums
