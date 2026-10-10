def combo(n,k):
    result=[]
    nums=list(range(1,n+1))
    curr_combo=[]
    start=0
    def helper(n,k,curr_combo,start):
        if len(curr_combo)==k:
            result.append(curr_combo.copy())
            return
        for i in range(start,len(nums)):
            pick=nums[i]
            curr_combo.append(pick)
            helper(n,k,curr_combo,i+1)
            curr_combo.pop(-1)
    helper(n,k,[],start)
    return result

print(combo(4,2))