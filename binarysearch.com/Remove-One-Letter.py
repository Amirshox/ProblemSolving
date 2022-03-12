class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1) + 1:
            return False
        s0 = iter(s0)
        s1 = iter(s1)
        return all(x in s0 for x in s1)
