class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                temp = []
                while stack and stack[-1] != '[':
                    temp.append(stack.pop()) 
                stack.pop() # popped '['
                string = ""
                while temp:
                    string += temp.pop()
                res = ""   
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                    
                res = string * int(num) 
                stack.append(res)
            else:
                stack.append(c)

        return "".join(stack)


        