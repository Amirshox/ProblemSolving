class Solution:
    def solve(self, typed, target):
        lt = len(target)
        j = 0
        prev = ""
        for t in typed:
            if j < lt and t == target[j]:
                j += 1
            elif t != prev:
                return False
            prev = t
        return j == lt
