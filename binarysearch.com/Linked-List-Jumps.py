class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


l4 = LLNode(val=1)
l3 = LLNode(val=4, next=l4)
l2 = LLNode(val=1, next=l3)
l1 = LLNode(val=2, next=l2)
l = LinkedList()
l.head = l1


class Solution:
    def solve(self, node):
        if node is None:
            return None
        temp, head = node, node
        while temp is not None:
            jump = temp.val
            save = temp  # To save the current node
            count = 0
            while count != jump and temp is not None:
                count += 1
                temp = temp.next
            save.next = temp
            # This is why we saved the initial node- so that we can attach the node found
        return head


s = Solution()
print(s.solve(node=l.head))
