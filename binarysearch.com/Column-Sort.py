class Solution:
    def solve(self, matrix):
        result = []
        res = list(zip(*matrix))  # Interchanging rows and columns so that it is easy to sort
        for i in res:
            l = list(i)
            l.sort()
            result.append(l)
        return list(zip(*result))  # Interchanging the rows and columns back
