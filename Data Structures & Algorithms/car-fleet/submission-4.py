class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        sorted_idx = sorted(range(n), key=lambda i:position[i])
        sorted_position = [position[i] for i in sorted_idx]
        sorted_speed = [speed[i] for i in sorted_idx]
        ans = 1
        meet_points = []
        for i in range(n - 2, -1, -1):
            p1, p2 = sorted_position[i], sorted_position[i + 1]
            s1, s2 = sorted_speed[i], sorted_speed[i + 1]
            if s1 <= s2:
                ans += 1
                meet_points.append(float("inf"))
            else:
                t = (p2 - p1)/(s1 - s2)
                meet_point = p1 + s1 * t
                meet_points.append(meet_point)
                if meet_point > target:
                    ans += 1
                else:
                    sorted_speed[i] = sorted_speed[i + 1]
                    sorted_position[i] = sorted_position[i + 1]
        return ans
