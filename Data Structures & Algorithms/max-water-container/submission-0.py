class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights)-1
        for k in range(len(heights)):
            if i == j:
                break
            r =  heights[i]
            l =  heights[j]

            min_h = min(r,l)

            area = max((j-i) * min_h, area)

            if  r < l:
                i +=1
            else:
                j -=1  

        return area              


