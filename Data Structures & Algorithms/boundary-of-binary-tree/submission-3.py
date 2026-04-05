# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_boundary = [root.val]
        def get_left_boundary(u):
            nonlocal left_boundary
            left_boundary.append(u.val)
            if u.left:
                get_left_boundary(u.left)
            elif u.right:
                get_left_boundary(u.right)
            else:
                left_boundary.pop()
        if root.left:
            get_left_boundary(root.left)
        right_boundary = []
        def get_right_boundary(u):
            nonlocal right_boundary
            right_boundary.append(u.val)
            if u.right:
                get_right_boundary(u.right)
            elif u.left:
                get_right_boundary(u.left)
            else:
                right_boundary.pop()
        if root.right:
            get_right_boundary(root.right)
        leaves = []
        def get_leaves(u):
            nonlocal leaves
            if u.left:
                get_leaves(u.left)
            if u.right:
                get_leaves(u.right)
            if not u.left and not u.right:
                leaves.append(u.val)
        if root.left or root.right:
            get_leaves(root)
        return left_boundary + leaves + list(reversed(right_boundary))