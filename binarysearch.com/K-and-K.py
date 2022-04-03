class Solution:
    def solve(self, nums):
        res = -1
        table = {}

        for n in nums:
            if -n in table or not n:
                res = max(res, abs(n))

            table[n] = True

        return res
