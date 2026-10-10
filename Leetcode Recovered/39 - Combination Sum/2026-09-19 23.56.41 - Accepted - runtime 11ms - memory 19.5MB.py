class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
            result=[]
            # Base Case
            def helper(candidates,target,curr_result,result,start):
                # start=0
                if sum(curr_result)==target:
                    result.append(curr_result.copy())
                    return
                for i in range(start,len(candidates)):
                    curr_result.append(candidates[i])
                    if sum(curr_result)>target:
                        curr_result.pop(-1)
                    else:
                        helper(candidates,target,curr_result,result,i)
                        curr_result.pop(-1)
            helper(candidates,target,[],result,0)
            return result

        