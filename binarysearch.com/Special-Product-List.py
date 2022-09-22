from math import prod


class Solution:
    def solve(self, nums):
        n = len(nums)

        left = [0] * n
        right = [0] * n
        result = [0] * n

        left[0] = 1
        right[n - 1] = 1

        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        for j in range(n - 2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]

        for i in range(n):
            result[i] = left[i] * right[i]

        return result


print(Solution().solve([1, 2, 3, 4, 5]))
