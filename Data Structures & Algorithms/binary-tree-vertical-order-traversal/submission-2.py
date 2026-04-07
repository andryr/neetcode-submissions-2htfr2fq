# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        x_coord = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, x = queue.popleft()
            x_coord[x].append(node.val)
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))
        return [x_coord[x] for x in sorted(x_coord.keys())]