class Solution(object):
    def minBitFlips(self, start, goal):
        count=0
        x=start^goal
        while x!=0:
            x=x&(x-1)
            count+=1
        return count
        