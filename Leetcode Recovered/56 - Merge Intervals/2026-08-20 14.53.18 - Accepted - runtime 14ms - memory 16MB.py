class Solution(object):
    def merge(self, nums):
        nums.sort()
        n=len(nums)
        unique=[]
        i=0
        current=nums[i]
        while i+1<n:
            if current[1]>=nums[i+1][0]:
                start=min(current[0],nums[i+1][0])
                end=max(current[1],nums[i+1][1])
                current=[start,end]
                i+=1
            else:
                unique.append(current)
                i+=1
                current=nums[i]
        if i<n:
            while i<n:
                unique.append(current)
                i+=1
        return unique
