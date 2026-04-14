class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        freq = [[] for _ in range(len(nums)+1)]
        res = []

        for n in nums:
            count[n] = count.get(n,0) + 1

        for n,f in count.items():
            freq[f].append(n)

        for i in range(len(nums),-1,-1):
            for digit in freq[i]:
                res.append(digit)
                if len(res) == k:
                    return res    
                






