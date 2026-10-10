class Solution(object):
    def singleNumber(self, nums):
        n=len(nums)
        x=0
        for i in range(n):
            x=x^nums[i]
        return x