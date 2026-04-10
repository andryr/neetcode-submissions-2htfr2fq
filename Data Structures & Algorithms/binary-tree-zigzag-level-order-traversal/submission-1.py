# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        ltr = True
        cur_level = [root] if root else []
        next_level = []
        while cur_level:
            for u in cur_level:
                children = (u.left, u.right) if ltr else (u.right, u.left)
                for v in children:
                    if v:
                        next_level.append(v)
            res.append([u.val for u in cur_level])
            cur_level = next_level[::-1]
            next_level = []
            ltr = not ltr
        return res



