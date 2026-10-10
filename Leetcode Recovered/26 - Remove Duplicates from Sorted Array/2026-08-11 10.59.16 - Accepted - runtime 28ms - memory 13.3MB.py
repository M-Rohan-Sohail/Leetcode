class Solution(object):
    def removeDuplicates(self, nums):
        unique=[]
        if len(nums)==0:
            return
        else:
            for num in nums:
                if num not in unique:
                    unique.append(num)
            nums[:]=unique
            return len(nums)
        