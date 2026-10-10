class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        lower=0
        upper=n-1
        lb=n
        while lower<=upper:
            mid=(lower+upper)//2     
            if nums[mid]>=target:
                lb=mid
                upper=mid-1
            else:
                lower=mid+1
        return lb
            