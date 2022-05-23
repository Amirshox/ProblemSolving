class Solution:
    def solve(self, nums):
        if len(nums) > 1:
            if nums[0] < nums[1]:
                for i in range(len(nums) - 1):
                    if nums[i] < nums[i + 1]:
                        continue
                    else:
                        return False
            elif nums[0] > nums[1]:
                for i in range(len(nums) - 1):
                    if nums[i] > nums[i + 1]:
                        continue
                    else:
                        return False
            else:
                return False
            return True
        return True
