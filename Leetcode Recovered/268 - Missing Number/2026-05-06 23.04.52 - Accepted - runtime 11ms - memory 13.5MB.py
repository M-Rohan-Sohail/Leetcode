class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expected_sum=[]
        for i in range(0,n+1):
            expected_sum.append(i)
        missing=sum(expected_sum) - sum(nums)
        return missing
        