class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for op in operations:
            
            match op:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case "C":
                    stack.pop()
                case "D":
                    val = stack[-1]
                    stack.append(2 * val)
                case _:
                    stack.append(int(op))
        sum = 0
        for val in stack:
            sum += val
        return sum    

        