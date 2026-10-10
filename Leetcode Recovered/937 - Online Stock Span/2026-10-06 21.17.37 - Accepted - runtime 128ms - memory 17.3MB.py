class StockSpanner(object):

    def __init__(self):
        self.result = []

    def next(self, price):

        span = 1

        while self.result and self.result[-1][0] <= price:

            span = span + self.result[-1][1]

            self.result.pop(-1)

        self.result.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)