class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # time,position
        positionSpeed ={}

        for i,p in enumerate(position):
            positionSpeed[p] = speed[i]
        
        position.sort()

        for p in position:
            time = (target-p)/positionSpeed[p]
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)    

        

        