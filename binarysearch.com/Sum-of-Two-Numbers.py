class Solution:
    def solve(self, nums, k):
        expected = set()
        for i in nums:
            if i not in expected:
                expected.add(k - i)
            else:
                return True
        return False
