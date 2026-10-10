class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        check_list=[]
        for i in range(0,n+1):
            check_list.append(i)
        for i in range(len(check_list)):
            if check_list[i] not in nums:
                return check_list[i]
        