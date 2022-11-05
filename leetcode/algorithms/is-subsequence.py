class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            try:
                t = t[t.index(c) + 1:]
            except ValueError:
                return False

        return True


print(Solution().isSubsequence('abc', 'ahbgdc'))