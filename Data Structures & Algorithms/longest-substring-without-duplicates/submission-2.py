class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        maxLen = 0
        l = 0

        for c in s:
            while c in subSet:
                subSet.remove(s[l])
                l+=1

            subSet.add(c)
            maxLen = max(maxLen,len(subSet))   
        return maxLen

        