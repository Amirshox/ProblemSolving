class Solution:
    def solve(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        for idx in range(n):
            if nums[idx] < 0 and k > 0:
                k -= 1
                nums[idx] *= -1

        if k & 1 == 1:
            return sum(nums) - 2 * min(nums)

        return sum(nums)
