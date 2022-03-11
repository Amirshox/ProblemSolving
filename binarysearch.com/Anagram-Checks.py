class Solution:
    def solve(self, s0, s1):
        if sorted(s0) == sorted(s1):
            return True
        return False
