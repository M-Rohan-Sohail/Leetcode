class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        if n==0:
            return nums
        elif n==1:
            return nums[0]
        else:
            sum=nums[0]
            max_sum=nums[0]
            for i in range(1,n):
                if nums[i]>=sum+nums[i]:
                    sum=nums[i]           
                else:
                  sum+=nums[i] 
                max_sum=max(sum,max_sum)
            return max_sum
