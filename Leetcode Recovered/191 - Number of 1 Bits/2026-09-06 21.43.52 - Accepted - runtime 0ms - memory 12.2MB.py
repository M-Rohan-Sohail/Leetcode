class Solution(object):
    def hammingWeight(self, num):
        count=0
        while num!=0:
            num=num&(num-1)
            count+=1
        return count