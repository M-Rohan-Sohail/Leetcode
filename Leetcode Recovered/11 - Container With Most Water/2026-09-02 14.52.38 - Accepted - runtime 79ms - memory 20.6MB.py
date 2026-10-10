class Solution(object):
    def maxArea(self, nums):
        n=len(nums)
        i=0
        j=n-1
        width=0
        max_water_level=0
        curr_water_level=0
        while i<j:
            if nums[i]<nums[j]:
                width=j-i
                curr_water_level=width*nums[i]
                max_water_level=max(max_water_level,curr_water_level)
                i+=1
            else:
                width=j-i
                curr_water_level=width*nums[j]
                max_water_level=max(max_water_level,curr_water_level)
                j-=1
        return max_water_level