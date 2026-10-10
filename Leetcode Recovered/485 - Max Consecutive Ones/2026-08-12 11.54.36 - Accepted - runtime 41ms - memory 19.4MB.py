class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        result=[]
        curr_consec=0
        for i in range(n):
            if nums[i]==1:
                curr_consec+=1
            else:
                curr_consec=0
            result.append(curr_consec)  
        return max(result)
        