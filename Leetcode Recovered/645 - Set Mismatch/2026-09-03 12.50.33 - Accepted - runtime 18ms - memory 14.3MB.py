class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        count_dict={}
        for num in nums:
            if num in count_dict:
                count_dict[num]+=1
            else:
                count_dict[num]=1
        for num in range(1,n+1):
            if num not in count_dict:
                missing=num
            if num in count_dict and count_dict[num]==2:
                duplicate=num
        return [duplicate,missing]
            