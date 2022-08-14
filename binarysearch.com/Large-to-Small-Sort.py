class Solution:
    def solve(self, nums):
        if (length := len(nums)) <= 1:
            return nums

        nums.sort()
        ls = []

        backHalf = nums[length - 1: (length - 1) // 2: -1]
        frontHalf = nums[:length // 2]

        for i in range(length // 2):
            ls.append(backHalf[i])
            ls.append(frontHalf[i])

        if length % 2 == 1:
            ls.append(nums[length // 2])

        return ls
