class Solution:
    def solve(self, nums):
        odd = sorted(filter(lambda x: x % 2, nums), reverse=True)
        even = sorted(filter(lambda x: not x % 2, nums))

        a = b = 0
        for i, v in enumerate(nums):
            if v % 2:
                nums[i] = odd[a]
                a += 1
            else:
                nums[i] = even[b]
                b += 1

        return nums
