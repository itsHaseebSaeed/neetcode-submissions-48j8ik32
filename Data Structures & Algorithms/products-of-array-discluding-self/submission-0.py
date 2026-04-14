class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backward = []
        res = []
        val = 1
        for n in nums:
            val *= n
            forward.append(val)
        val = 1
        for i in range(len(nums)-1,-1,-1):
            val *= nums[i]
            backward.append(val)
        backward.reverse()    

        for i in range(len(nums)):
            f = 1
            b = 1
            if i == 0:
                f = 1
            else:
                f = forward[i-1]    
            if i == len(nums)-1:
                b = 1
            else:
                b = backward[i+1]
            res.append(f*b)
        return res    
