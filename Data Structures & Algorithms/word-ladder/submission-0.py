class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_map = {}
        full_word_list = wordList + [beginWord]
        for word in full_word_list:
            for i in range(len(word)):
                word_map.setdefault(word[:i] + "_" + word[i+1:], []).append(word)
        
        adj_list = {}
        for word in full_word_list:
            neighbours = []
            for i in range(len(word)):
                neighbours.extend(word_map[word[:i] + "_" + word[i+1:]])
            adj_list[word] = set(w for w in neighbours if w != word)
        
        visited = set()
        queue = deque([(1, beginWord)])
        while queue:
            dist, word = queue.popleft()
            visited.add(word)
            if word == endWord:
                return dist
        
            for neighbour in adj_list[word]:
                if neighbour in visited:
                    continue
                queue.append((dist + 1, neighbour))
        return 0
        
