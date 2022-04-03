class Solution:
    def solve(self, n):
        n_list = list(map(int, str(n)))
        for i, v in enumerate(n_list):
            if v < 3:
                n_list[i] = 3
                return int(''.join(map(str, n_list)))
        return n
