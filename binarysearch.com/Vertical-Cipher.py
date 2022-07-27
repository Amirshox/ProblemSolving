class Solution:
    def solve(self, s, k):
        return [s[idx::k] for idx in range(k)]
