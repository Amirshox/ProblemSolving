class Solution:
    def solve(self, nums):
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(0)
            else:
                result.append(min(nums[:i]))
        return result
