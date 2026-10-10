class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[]
        curr_result=[]
        def helper(nums,curr_result):
            if len(curr_result)==len(nums):
                result.append(curr_result.copy())
                return
            for num in nums:
                if num not in curr_result:
                    curr_result.append(num)
                    helper(nums,curr_result)
                    curr_result.pop(-1)
        helper(nums,curr_result)
        return result
            