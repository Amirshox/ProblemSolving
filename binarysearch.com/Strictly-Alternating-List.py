class Solution:
    def solve(self, a):
        return a[0] < a[1] and all(a[i - 1] != a[i] for i in range(1, len(a)))
