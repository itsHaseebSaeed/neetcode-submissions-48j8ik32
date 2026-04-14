class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freqMap = {}
        l = 0
        for r,c in enumerate(s):
            freqMap[c] = freqMap.get(c,0) + 1 
            m_f_c = 0
            for val in freqMap.values():
                m_f_c = max(m_f_c,val)

            while (r - l + 1) - m_f_c > k:
                freqMap[s[l]] = freqMap.get(s[l],0) - 1 
                l += 1

            longest = max(longest, r - l + 1)

        return longest    

        # AAABABBBBBBB k = 2


        