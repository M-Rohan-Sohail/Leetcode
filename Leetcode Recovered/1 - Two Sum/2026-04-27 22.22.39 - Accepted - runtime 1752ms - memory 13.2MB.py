class Solution(object):
    def twoSum(self,nums,target):
        n=len(nums)
        for i in range (0,n):
            key=nums[i]
            for j in range(i+1,n):
                if (key+nums[j])==target:
                    return [i,j]
        