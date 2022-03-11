class Solution:
    def solve(self, s):
        counter = 0
        pointer = s[0]
        result = ""
        for i, ch in enumerate(s):
            if ch == pointer:
                counter += 1
            else:
                result += f"{counter}{s[i - 1]}"
                pointer = ch
                counter = 1
        result += f"{counter}{s[-1]}"
        return result
