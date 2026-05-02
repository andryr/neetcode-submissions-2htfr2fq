# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left > 1:
            return ListNode(head.val, self.reverseBetween(head.next, left - 1, right - 1))
        stack = []
        cur = head
        for i in range(left, right + 1):
            new_node = ListNode(cur.val)
            if stack:
                new_node.next = stack[-1]
            stack.append(new_node)
            cur = cur.next
        stack[0].next = cur
        return stack[-1]