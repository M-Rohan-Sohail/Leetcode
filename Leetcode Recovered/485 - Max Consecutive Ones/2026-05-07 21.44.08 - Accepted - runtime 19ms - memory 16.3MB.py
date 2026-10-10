class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        largest=0
        result_main=0
        for i in range(n):
            if nums[i]==1:
                largest+=1
            else:
                result_main=max(largest,result_main)
                largest=0
        return max(largest,result_main)