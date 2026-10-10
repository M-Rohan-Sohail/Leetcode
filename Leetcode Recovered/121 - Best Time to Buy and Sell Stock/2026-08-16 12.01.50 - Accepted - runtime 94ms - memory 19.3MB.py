class Solution(object):
    def maxProfit(self, nums):
        n=len(nums)
        min_stock=nums[0]
        profit=0
        for i in range(1,n):
            if nums[i]<min_stock:
                min_stock=nums[i]
            else:
                profit=max(profit,nums[i]-min_stock)
        return profit   