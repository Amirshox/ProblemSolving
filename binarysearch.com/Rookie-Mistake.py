class Solution:
    def solve(self, s: str):
        left, right = s.split("R")
        return "B" not in left or "B" not in right


s = Solution()
print(s.solve(s="...R."))
