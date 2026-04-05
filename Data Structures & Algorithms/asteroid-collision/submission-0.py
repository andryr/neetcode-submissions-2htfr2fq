class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            explode = False
            while stack:
                other_asteroid = stack[-1]
                if -asteroid >= other_asteroid:
                    stack.pop()
                if -asteroid <= other_asteroid:
                    explode = True
                    break
            if not stack and not explode:
                ans.append(asteroid)
        ans.extend(stack)
        return ans