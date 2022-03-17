class Solution:
    def solve(self, rooms, target):
        for i in rooms:
            if target > i:
                continue
            else:
                return i
        return -1
