"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        queue = deque([root])
        res = [root.val]
        while queue:
            u = queue.popleft()
            if not u:
                continue
            res.append(None)
            for v in u.children:
                queue.append(v)
                res.append(v.val)
        res =  ",".join(str(u) for u in res)

        print(res)
        return res
        

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        node_values = list(reversed([int(u) if u != "None" else None for u in data.split(",")]))

        root = Node(node_values.pop())
        node_values.pop()
        cur_level = []
        prev_level = [root]

        i = 0
        while node_values:
            u = node_values.pop()

            if u is None:
                if i + 1 >= len(prev_level):
                    i = 0
                    prev_level = cur_level
                    cur_level = []
                else:
                    i += 1
            else:
                node = Node(u)
                prev_level[i].children.append(node)
                cur_level.append(node)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
