class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        res = 0

        for n in nums:
            if n not in numSet:
                numSet.add(n)

        for n in nums:
            if n-1 in numSet:
                continue
            num = n
            count = 0
            while num in numSet:
                count+=1
                res = max(res,count)
                num+=1

            
        return res    

        