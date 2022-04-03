from collections import Counter


class Solution:
    def solve(self, s):
        return len(Counter(s)) == len(s)
