def csII(k,n):
    result=[]
    num_list=list(range(1,10)) # List Range 1-9
    curr_sum=[]
    start=0
    def helper(k,n,curr_sum,result,start):
        if sum(curr_sum)==n and len(curr_sum)==k:
            result.append(curr_sum.copy())
            return
        for i in range(start,len(num_list)):
            pick=num_list[i]
            curr_sum.append(pick)
            if sum(curr_sum)>n:
                curr_sum.pop(-1)
            else:
                helper(k,n,curr_sum,result,i+1)
                curr_sum.pop(-1)
    helper(k,n,[],result,start)
    return result

print(csII(3,9))
