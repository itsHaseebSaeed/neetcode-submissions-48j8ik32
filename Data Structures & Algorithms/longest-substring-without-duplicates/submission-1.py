class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        charMap = {}
        l=0
        for r,c in enumerate(s):
            if c in charMap:
                l = max(l, charMap[c] + 1)
            charMap[c] = r
            longest = max(longest, r-l+1)
                
        return longest


        