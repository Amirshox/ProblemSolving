# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node):
        result = 0
        while node:
            result += 1
            node = node.next

        return result