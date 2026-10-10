class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        current_sum=nums[0]
        max_sum=nums[0]
        for i in range(1,n):
            if nums[i]>=current_sum+nums[i]:
                current_sum=nums[i]
            else:
                current_sum+=nums[i]
            max_sum=max(current_sum,max_sum)
        return max_sum
        