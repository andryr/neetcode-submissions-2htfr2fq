# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list_1, list_2):
            res = ListNode()
            cur = res
            while list_1 and list_2:
                if list_1.val <= list_2.val:
                    cur.next = ListNode(list_1.val)
                    list_1 = list_1.next
                else:
                    cur.next = ListNode(list_2.val)
                    list_2 = list_2.next
                cur = cur.next
            if list_1:
                cur.next = list_1
            if list_2:
                cur.next = list_2
            return res.next
        if not lists:
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    res = merge_two_lists(lists[i], lists[i + 1])
                else:
                    res = lists[i]
                merged_lists.append(res)
            lists = merged_lists
        return lists[0]
        
