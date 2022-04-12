class Solution:
    def solve(self, s):
        A = list(s)
        for i, c in enumerate(A):
            if c == "?":
                for d in "123":
                    A[i] = d
                    if i - 1 >= 0 and A[i] == A[i - 1]:
                        continue
                    if i + 1 < len(A) and A[i] == A[i + 1]:
                        continue
                    break

        return "".join(A)

