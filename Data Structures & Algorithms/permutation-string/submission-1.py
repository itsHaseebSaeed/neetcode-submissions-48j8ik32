class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        s1map = {}
        s2_map = {}
        l = 0


        for c in s1:
            s1map[c] = 1 + s1map.get(c,0)   

            # {a:1,b:1,c:1}
        # if c in map_s1 (don't move) l  
        for r,c in enumerate(s2):
            if c in s1map:
                s2_map[c] = 1 + s2_map.get(c,0)
                while s2_map.get(c,0) > s1map.get(c,0):
                    s2_map[s2[l]] -=1
                    l+=1 
                if (r-l+1) == len(s1):
                    return True 
            else:
                l = r + 1    
                s2_map={}
                   
        return False
        