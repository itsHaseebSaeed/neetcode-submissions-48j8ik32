class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l,r):
            left,right = l,r

            if nums[left] >= target or nums[right] <= target:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:    
                    return -1

            while right - left > 1:
                mid = (left+right ) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid   

                if nums[right] == target:
                    return right   
            return -1

        # find the lowest number # binary search
        # if the number is not first then the prev num is going to be highest
        # low - last index # binary
        
        l,r = 0, len(nums) - 1
        if nums[l] > nums[r]:
            while r - l > 1:
                mid = (r+l)//2
                if nums[mid] >= nums[l]:
                    l = mid
                else:
                    r = mid    

            low_index = r # till end of array
            high_index = r - 1 # from start of array
            res1 = binary_search(low_index,len(nums)-1)
            res2 = binary_search(0,high_index)

            if res1 != -1:
                return res1
            elif res2 != -1:
                return res2
            else:
                return -1        
        else:
            return binary_search(l,r)


