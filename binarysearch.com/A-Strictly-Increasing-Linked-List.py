class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


l4 = LLNode(val=9)
l3 = LLNode(val=9, next=l4)
l2 = LLNode(val=9, next=l3)
l1 = LLNode(val=5, next=l2)
l = LinkedList()
l.head = l1


class Solution:
    def solve(self, head):
        curr = head
        while curr.next is not None:
            if curr.val >= curr.next.val:
                return False
            curr = curr.next
        return True


s = Solution()
print(s.solve(head=l.head))
