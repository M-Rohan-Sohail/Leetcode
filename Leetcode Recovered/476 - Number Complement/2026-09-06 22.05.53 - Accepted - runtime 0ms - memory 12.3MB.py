class Solution(object):
    def findComplement(self, num):
            count_num=num
            i=0
            while count_num>0:
                count_num=count_num>>1
                num=num^(1<<i)
                i+=1
            return num
        
        