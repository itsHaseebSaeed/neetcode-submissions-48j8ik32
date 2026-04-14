class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [2, 4, -4]

        stack = []

        for a in asteroids:

            if not stack:
                stack.append(a)
            else:
                if a < 0:
                    flag = True
                    while stack and stack[-1] > 0:
                        if abs(stack[-1]) < abs(a):
                            stack.pop()
                        elif abs(stack[-1]) == abs(a):
                            stack.pop()
                            flag = False
                            break    
                        else:
                            flag = False
                            break
                    if flag:
                        stack.append(a)
                else:
                    stack.append(a)

        return stack