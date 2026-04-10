# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            u1 = l1 if l1 else ListNode(0)
            u2 = l2 if l2 else ListNode(0)
            s = u1.val + u2.val + carry
            carry = s // 10
            s = s % 10
            return ListNode(s, add(u1.next, u2.next, carry))
        return add(l1, l2, 0)
            