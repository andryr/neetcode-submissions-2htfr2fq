import functools

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.cache
        def compare(i, j, word1, word2):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return compare(i + 1, j + 1, word1, word2)
            
            return 1 + min(compare(i + 1, j + 1, word1, word2), compare(i + 1, j, word1, word2), compare(i, j + 1, word1, word2))
        return compare(0, 0, word1, word2)

            

            