class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        def neighbors(x, y):
            return [
                (x + 1, y + 2),
                (x + 2, y + 1),
                (x + 2, y - 1),
                (x + 1, y - 2),
                (x - 1, y - 2),
                (x - 2, y - 1),
                (x - 2, y + 1),
                (x - 1, y + 2)
            ]
        
        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}
        while queue:
            xx, yy, moves = queue.popleft()
            if (xx, yy) == (x, y):
                return moves
            for xxx, yyy in neighbors(xx, yy):
                if (xxx, yyy) in visited or xxx < -1 or yyy < -1:
                    continue
                visited.add((xxx, yyy))
                queue.append((xxx, yyy, moves + 1))
        return 999999999