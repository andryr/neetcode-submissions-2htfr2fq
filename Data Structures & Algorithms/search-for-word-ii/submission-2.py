class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children.setdefault(c, Trie())
        cur.is_word = True
        cur.word = word
    

def dfs(i, j, board, trie, word_set, visited):
    m, n = len(board), len(board[0])
    if trie.is_word:
        word_set.add(trie.word)
    for k, l in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if not (0 <= k < m and 0 <= l < n) or (k, l) in visited:
            continue
        letter = board[k][l]
        if letter not in trie.children:
            continue
        visited.add((k, l))
        dfs(k, l, board, trie.children[letter], word_set, visited)
        visited.remove((k, l))

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])
        ans = set()
        for i in range(m):
            for j in range(n):
                letter = board[i][j]
                if letter not in trie.children:
                    continue
                dfs(i, j, board, trie.children[letter], ans, {(i, j)})
        return list(ans)
