"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        def dfs(node, right):
            node.next = right
            if not node.left:
                return
            dfs(node.left, node.right)
            dfs(node.right, right.left if right else None)
        dfs(root, None)
        return root