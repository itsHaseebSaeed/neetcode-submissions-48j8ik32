class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            countMap[n] = 1 + countMap.get(n,0)
        for num, cnt in countMap.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res        



        