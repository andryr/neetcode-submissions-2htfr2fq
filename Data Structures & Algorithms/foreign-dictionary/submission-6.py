from string import ascii_lowercase

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letter_set = set(letter for word in words for letter in word )
        graph = defaultdict(set)
        num_pred = defaultdict(int)
        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]
            for a, b in zip(word_1, word_2):
                if a == b:
                    continue
                if b not in graph[a]:
                    graph[a].add(b)
                    num_pred[b] += 1
                break
            else:
                if len(word_1) > len(word_2):
                    return ""

        queue = deque()
        for letter in letter_set:
            if num_pred[letter] == 0:
                queue.append(letter)

        seen = set()
        res = []
        while queue:
            cur = queue.popleft()
            seen.add(cur)
            res.append(cur)
            for succ in graph[cur]:
                num_pred[succ] -= 1
                if num_pred[succ] == 0:
                    queue.append(succ)

        if any(num_pred[letter] > 0 for letter in letter_set):
            return ""
        used_letters = set(res)
        for letter in letter_set:
            if letter not in used_letters:
                res.append(letter)
        return "".join(res)

                
        
        
                