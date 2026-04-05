# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def rec_merge_sort(pairs, start, end):
            if end - start <= 1:
                return pairs
            mid = (start + end) // 2
            rec_merge_sort(pairs, start, mid)
            rec_merge_sort(pairs, mid, end)
            return merge(pairs, start, mid, end)

        def merge(pairs, start, mid, end):
            left = pairs[start:mid]
            right = pairs[mid:end]
            i, j = 0, 0
            k = start
            res = []
            while i < len(left) and j < len(right):
                if left[i].key <= right[j].key:
                    pairs[k] = left[i]
                    i += 1
                else:
                    pairs[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                pairs[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                pairs[k] = right[j]
                j += 1
                k += 1
            
        rec_merge_sort(pairs, 0, len(pairs))
        return pairs