class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        neg_stack = []
        for i in asteroids:
            if i > 0 :
                stack.append(i)
            else:
                while stack and stack[-1] < abs(i):
                    stack.pop()
                if not stack:
                    neg_stack.append(i)
                elif stack[-1] == abs(i):
                    stack.pop()
        return neg_stack+stack