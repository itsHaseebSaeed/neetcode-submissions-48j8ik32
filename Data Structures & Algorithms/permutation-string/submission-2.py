class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLen = len(s1)
        r = 0
        l = 0
        s1CountMap = {}

        for c in s1:
            s1CountMap[c] = s1CountMap.get(c,0) + 1

        s2countMap = {}

        # leccbaee

        while r < len(s2):
            if s2[r] not in s1CountMap:
                r += 1
                l = r
                s2countMap = {}
                continue

            s2countMap[s2[r]] = s2countMap.get(s2[r],0) + 1
            r += 1

            if r - l  == windowLen:
                flag = 0
                for key,val in s1CountMap.items():
                    if s2countMap.get(key,0) != val:
                        flag = 1
                        break
                s2countMap[s2[l]] = s2countMap.get(s2[l],0) - 1
                l += 1        
                if flag == 0:        
                    return True        


        return False
            # lecabee
    





            



        