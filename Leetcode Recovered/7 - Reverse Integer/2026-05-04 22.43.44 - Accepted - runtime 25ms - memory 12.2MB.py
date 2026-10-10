class Solution(object):
    def reverse(self, x):
        result = 0
        # Determine the sign and work with absolute value to simplify modulo
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            last = x % 10
            x //= 10
            
            # Check for overflow (214748364 is 2^31 // 10)
            if result > 214748364 or (result == 214748364 and last > 7):
                return 0
            
            # Since we're using abs(x), we only need to check the upper bound.
            # The negative limit (-8) is covered by the symmetry of the logic.
            result = (result * 10) + last
            
        return result * sign