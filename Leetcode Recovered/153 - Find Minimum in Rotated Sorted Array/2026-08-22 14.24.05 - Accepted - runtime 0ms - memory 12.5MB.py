class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        i=0
        min_num=nums[i]
        while i<n:
            min_num=min(min_num,nums[i])
            i+=1
        return min_num
        