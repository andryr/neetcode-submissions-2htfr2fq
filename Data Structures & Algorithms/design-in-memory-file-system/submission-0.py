class Node:
    def __init__(self, is_file=False):
        self.children = {}
        self.is_file = is_file
        self.contents = None if not is_file else ""

class FileSystem:

    def __init__(self):
        self.root = Node()
        

    def ls(self, path: str) -> List[str]:
        parts = [part for part in path.split("/") if len(part) > 0]
        cur = self.root
        for part in parts:
            cur = cur.children[part]
        if cur.is_file:
            return [parts[-1]]
        return sorted(cur.children.keys())

    def mkdir(self, path: str) -> None:
        parts = [part for part in path.split("/") if len(part) > 0]
        cur = self.root
        for part in parts:
            cur = cur.children.setdefault(part, Node())

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = [part for part in filePath.split("/") if len(part) > 0]
        cur = self.root
        for part in parts:
            cur = cur.children.setdefault(part, Node(is_file=True))
        cur.contents = cur.contents + content

    def readContentFromFile(self, filePath: str) -> str:
        parts = [part for part in filePath.split("/") if len(part) > 0]
        cur = self.root
        for part in parts:
            cur = cur.children[part]
        return cur.contents
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
