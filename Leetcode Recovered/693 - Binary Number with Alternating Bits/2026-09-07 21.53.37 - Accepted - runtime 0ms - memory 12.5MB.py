class Solution(object):
    def hasAlternatingBits(self, num):
            x=num^(num>>1)
            return (x&(x+1))==0
        