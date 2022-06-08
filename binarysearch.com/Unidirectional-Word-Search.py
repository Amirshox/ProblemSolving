class Solution:
    def solve(self, board, word):
        n, m = len(board), len(board[0])
        for i in range(m):
            row = ''
            for j in range(n):
                if word in ''.join(board[j]):
                    return True
                row += board[j][i]
            if word in row:
                return True
        return False


board = [
    ["x", "z", "d", "x"],
    ["p", "g", "u", "x"],
    ["k", "j", "z", "d"]
]
word = "xxd"

s = Solution()
print(s.solve(board, word))
