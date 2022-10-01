class Solution:
    def solve(self, s, t):
        ans = len(t)
        for i in range(len(s) - len(t) + 1):
            a = len(t)
            for j in range(len(t)):
                if t[j] == s[i + j]:
                    a -= 1
            ans = min(ans, a)
        return ans