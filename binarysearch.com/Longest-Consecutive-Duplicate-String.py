class Solution:
    def solve(self, s):
        counter = 0
        if len(s) == 0:
            return 0
        pointer = s[0]
        result = 0
        for ch in s:
            if ch == pointer:
                counter += 1
            else:
                counter = 1
                pointer = ch
            if counter > result:
                result = counter
        return result
