class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)+1
        sum_list=[]
        for i in range (n):
            sum_list.append(i)
        missing=sum(sum_list)-sum(nums)
        return missing