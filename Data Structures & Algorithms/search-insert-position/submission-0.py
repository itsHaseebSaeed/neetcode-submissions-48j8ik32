class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [-1,0,2,4,6,8]
        #   l
        #             r
        #         Mid  
        l,r = 0,len(nums)-1
        if nums[l] >= target or nums[r] < target:
            if nums[l] >= target:
                return 0
            return r + 1

        while r-l > 1:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
                
        if nums[r] == target:
            return r

        
        return r

            