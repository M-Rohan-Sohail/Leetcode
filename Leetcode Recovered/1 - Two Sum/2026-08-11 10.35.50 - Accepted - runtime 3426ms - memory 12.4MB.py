class Solution(object):
    def twoSum(self, nums, target):
            n=len(nums)
            i=0
            j=1
            while i<n and j<n:
                if nums[i]+nums[j]==target:
                    return [i,j]
                j+=1
                if j==n:
                    i+=1
                    j=i+1
