import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        i, j = idx - 1, idx
        while k:
            if j >= len(arr) or i >= 0 and x - arr[i] <= arr[j] - x:
                i -= 1
            else:
                j += 1
            k -= 1
        return arr[i + 1:j]