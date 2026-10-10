class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)
        nums.sort()
        count=1
        max_count=1
        if n==0:
            return 0
        else:
            for i in range(n-1):
                if nums[i+1]==nums[i]:
                      pass
                elif  nums[i+1]==nums[i]+1:
                            count+=1
                            max_count=max(max_count,count) 
                else:
                      count=1            
            return max_count
            