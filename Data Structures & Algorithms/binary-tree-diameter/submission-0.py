# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return -1, -1
            diam_l, diam_l_root = helper(root.left)
            diam_r, diam_r_root = helper(root.right)

            return max(max(diam_l, diam_r), diam_l_root + diam_r_root + 2), max(diam_l_root + 1, diam_r_root + 1)
        return helper(root)[0]