class Solution:
    def solve(self, n):
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                result.append('clap')
            elif '3' in str(i) or '6' in str(i) or '9' in str(i):
                result.append('clap')
            else:
                result.append(str(i))
        return result
