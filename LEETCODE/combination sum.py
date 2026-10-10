def cs(candinate,target):
    result=[]
    # Base Case
    def helper(candinate,target,curr_result,result,start):
        # start=0
        if sum(curr_result)==target:
            result.append(curr_result.copy())
            return
        for i in range(start,len(candinate)):
            curr_result.append(candinate[i])
            if sum(curr_result)>target:
                curr_result.pop(-1)
            else:
                helper(candinate,target,curr_result,result,i)
                curr_result.pop(-1)
    helper(candinate,target,[],result,0)
    return result

num=[2,3,6,7]
print(cs(num,7))

                