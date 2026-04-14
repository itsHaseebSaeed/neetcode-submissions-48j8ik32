class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def m_works(mid):
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            return hours <= h    

        l,r = 0, max(piles)

        while r - l  > 1:
            mid = (r+l)//2
            if m_works(mid):
                r = mid
            else:
                l = mid
                    
        return r

        
        