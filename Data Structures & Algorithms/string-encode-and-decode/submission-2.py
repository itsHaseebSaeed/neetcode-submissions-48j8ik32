class Solution:
    
    def encode(self, strs: List[str]) -> str:
        returnString = ''
        for s in strs:
            slen = len(s)
            returnString += str(slen) + '#' + s
        return returnString

# 4#neet4#code4#love3#you

    def decode(self, s: str) -> List[str]:
        returnArray = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            returnArray.append(s[j+1:j+1+length])  
            i = j + 1 + length   

        return returnArray
