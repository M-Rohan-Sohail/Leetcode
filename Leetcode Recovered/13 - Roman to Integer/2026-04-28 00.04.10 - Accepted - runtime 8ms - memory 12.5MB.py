class Solution(object):
    def romanToInt(self, s):
            vals = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
            prev_int=0
            result=0
            for ch in reversed(s):
                    curr=vals[ch]
                    if curr < prev_int:
                        result -= curr
                    else:
                        result +=curr
                    prev_int=curr
            return result
                    