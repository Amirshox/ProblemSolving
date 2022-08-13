# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node):
        result = ""
        while node:
            result += str(node.val)
            node = node.next
        return int(result, 2)
