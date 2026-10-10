class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        sett=[]
        subset=[]
        for mask in range(2**n):
            for i in range(n):
                if mask&(1<<i):
                    subset.append(nums[i])
            sett.append(subset)
            subset=[]
        return sett
        