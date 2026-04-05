# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def rec_quick_sort(start, end):
            if start >= end:
                return
            k = partition(start, end)
            rec_quick_sort(start, k - 1)
            rec_quick_sort(k + 1, end)

        def partition(start, end):
            pivot = pairs[end]

            i = start
            for j in range(start, end):
                if pairs[j].key < pivot.key:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    i += 1
            
            pairs[i], pairs[end] = pairs[end], pairs[i]
            return i
        rec_quick_sort(0, len(pairs) - 1)
        return pairs