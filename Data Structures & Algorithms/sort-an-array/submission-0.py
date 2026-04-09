class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, start, mid, end):
            res = []
            i, j = start, mid
            while i < mid and j < end:
                if nums[i] <= nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            res.extend(nums[i:mid])
            res.extend(nums[j:end])
            nums[start:end] = res
        
        def merge_sort(nums, start, end):
            if start + 1 >= end:
                return
            mid = (start + end) // 2
            merge_sort(nums, start, mid)
            merge_sort(nums, mid, end)
            merge(nums, start, mid, end)
        
        merge_sort(nums, 0, len(nums))
        return nums

        