class Solution:
    def solve(self, nums):
        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            if i + nums[i] >= goal:
                goal = 1

        return goal == 0
