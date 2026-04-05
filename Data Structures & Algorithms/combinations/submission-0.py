class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combine_rec(i, n, k, cur_comb):
            nonlocal res
            if k == 0:
                res.append(list(cur_comb))
                return
            if i > n:
                return    
            cur_comb.append(i)
            combine_rec(i + 1, n, k - 1, cur_comb)
            cur_comb.pop()
            combine_rec(i + 1, n, k, cur_comb)
        combine_rec(1, n, k, [])
        return res