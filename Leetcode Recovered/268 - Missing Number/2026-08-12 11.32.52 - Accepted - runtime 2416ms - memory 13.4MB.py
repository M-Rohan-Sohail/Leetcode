class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)+1
        find_list=[]
        for i in range(n):
            find_list.append(i)
        for lost_num in find_list:
            if lost_num not in nums:
                return lost_num