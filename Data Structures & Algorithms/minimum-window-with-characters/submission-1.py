class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res
        tMap = {}
        sMap = {}
        for c in t:
            tMap[c] = 1 + tMap.get(c,0)   

        # YYZYYYXAZV
        matched = 0
        l = 0    

        for r,c in enumerate(s):
            if c in tMap:
                sMap[c] = 1 + sMap.get(c,0) 
                if sMap[c] <= tMap[c]:
                    matched += 1

            while l < len(s) and(matched == len(t) or s[l] not in tMap or sMap.get(s[l],0) > tMap.get(s[l],0)):
                if s[l] in sMap:
                    if matched == len(t) and (len(res) == 0 or r-l+1 < len(res)):
                        res = s[l:r+1]   
                    if sMap[s[l]] ==  tMap[s[l]] :
                        matched -= 1
                    sMap[s[l]] = sMap.get(s[l],0) - 1
                l+=1

        return res   
      