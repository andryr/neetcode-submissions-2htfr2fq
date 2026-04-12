class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False
    
    def insert(self, path):
        path = path.split("/")[1:]
        cur = self
        for p in path:
            cur = cur.children.setdefault(p, TrieNode())
        cur.is_leaf = True

    def get_folders(self):
        folders = []
        for folder, child in self.children.items():
            if child.is_leaf:
                folders.append([folder])
            else:
                subfolders = child.get_folders()
                folders.extend([[folder] + subfolder for subfolder in subfolders])
        return folders
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for f in folder:
            root.insert(f)
        return ["/" + "/".join(f) for f in root.get_folders()]