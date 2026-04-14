class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # edge case where the token length is 1

        stack = []

        for c in tokens:
            if self.isOperator(c):
                a = int(stack.pop())
                b = int(stack.pop())
                res = self.Operation(b,a,c)
                stack.append(str(res))
            else:
                stack.append(c)
        return int(stack.pop())      


    def isOperator(self, val:str) -> bool:
        operators = {"+", "*", "-", "/"}
        if val in operators:
            return True
        else:
            return False    

    def Operation(self, val1:int, val2:int, operator:str) -> int:
        match operator:
            case "+":
                return val1 + val2
            case "-":
                return val1 - val2
            case "*":
                return val1 * val2
            case "/":
                return int(float(val1 / val2))
                
                
                    

        