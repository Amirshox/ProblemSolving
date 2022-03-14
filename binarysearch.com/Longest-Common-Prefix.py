class Solution:
    def solve(self, words):
        prefix = ""
        words = sorted(words)
        for i, word in enumerate(words):
            prefix += word[i]
            if prefix:
                pass
        return words


s = Solution()
print(s.solve(['asdferf', 'asdasd', 'asdqweqwws']))
