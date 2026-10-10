class Solution(object):
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        min_size=n
        int_len=0
        sum=0
        start=0
        i=0
        is_found=False
        while i<n:
            sum+=nums[i]
            int_len+=1
            i+=1
            while sum>=target:
                min_size=min(min_size,int_len)
                sum-=nums[start]
                start+=1
                int_len-=1
                is_found=True
        if is_found:
            return min_size
        else:
            return 0