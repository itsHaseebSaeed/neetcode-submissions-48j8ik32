class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[target - nums[i]] = i

        # 4 index 0
        for i,n in enumerate(nums):
            if  n in hashMap:
                if i == hashMap[n]:
                    continue
                return [i, hashMap[n]]

            

        
        

        