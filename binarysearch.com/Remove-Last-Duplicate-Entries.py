class Solution:
    def solve(self, nums):
        res = []
        first = {}
        last = {}

        for idx, num in enumerate(nums):
            if num not in first:
                first[num] = idx
            last[num] = idx

        for idx, num in enumerate(nums):
            if first[num] == last[num]:
                res.append(num)
                continue
            if last[num] != idx:
                res.append(num)
        return res
