class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        curr_subset=[]
        start=0
        def helper(nums,curr_subset,start):
            result.append(curr_subset.copy())
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                else:
                    curr_pick=nums[i]
                    curr_subset.append(curr_pick)
                    helper(nums,curr_subset,i+1)
                    curr_subset.pop(-1)
        helper(nums,curr_subset,start)
        return result
