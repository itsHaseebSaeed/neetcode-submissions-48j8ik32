class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][1] <= price:
            span += self.stack[-1][0]
            self.stack.pop()
            
        self.stack.append((span,price))    
        return span




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# [100], [80], [79], [60], [80], [60], [75], [85]
# [100-0, 85-7, 75-8, 96]