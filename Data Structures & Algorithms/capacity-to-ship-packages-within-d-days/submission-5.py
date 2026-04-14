class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # [1,2,3,4,5] -> 5 to 15
        # days utilized == 4
        # 5,6,7,8,9,10,..15

        def can_ship(cap):
            running_sum = 0
            d = 0
            for w in weights:
                if running_sum + w > cap:
                    running_sum = w
                    d += 1
                else:
                    running_sum += w 
            if running_sum > 0:
                d +=1
            return d <= days    


        sum_w = 0
        max_w = 0
        
        for w in weights:
            sum_w += w
            max_w = max(max_w,w)

        l,r = max_w,sum_w
        res = sum_w
        while r - l > 1:
            mid = (r+l) // 2
        
            if can_ship(mid):
                res = min(res,mid)
                r = mid
            else:
                l = mid

        if can_ship(l):
            return l

        return res


                



