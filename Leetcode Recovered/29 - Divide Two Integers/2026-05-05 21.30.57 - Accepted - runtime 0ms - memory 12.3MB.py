class Solution(object):
    def divide(self, x, y):
        zx = abs(x)
        zy = abs(y)
        quotient = 0

        MAX_INT = 2147483647
        MIN_INT = -2147483648

        # overflow cases (keep yours)
        if x == MIN_INT and y == -1:
            return MAX_INT

        # sign handling (moved outside loop)
        sign = -1 if (x < 0) ^ (y < 0) else 1

        while zx >= zy:
            temp = zy
            multiple = 1

            # doubling (main fix)
            while zx >= (temp << 1): # temp<<1 actually works as temp*2 
                temp <<= 1
                multiple <<= 1

            zx -= temp
            quotient += multiple

        # apply sign (no multiplication)
        if sign == -1:
            quotient = -quotient

        return quotient