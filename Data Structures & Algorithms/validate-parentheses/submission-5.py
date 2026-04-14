class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pthMap = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }

        for c in s:
            if not self.isClosing(c):
                stack.append(c)
            else:
                if len(stack) > 0:
                    last = stack.pop()
                    if pthMap[last] != c:
                        return False
                else:
                    return False        
        return len(stack) == 0


    def isClosing(self, s:str) -> bool:
        if s == '}' or s == ']' or s == ')':
            return True
        else:
            return False    