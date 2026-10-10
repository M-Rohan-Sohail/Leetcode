class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)
        result=[]
        if n==0:
            return [-1,-1]
        if n==1 and nums[0]==target:
            return [0,0]
        for i in range(n):
            if nums[i]==target:
                result.append(i)
        if result==[]:
            return [-1,-1]
        else:
            return [result[0],result[-1]]