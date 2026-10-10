def vp(n):
    result=[]
    curr_result=[]
    open_used=0
    closed_used=0
    parnthesis=["(",")"]
    def helper(n,curr_result,open_used,closed_used):
        if len(curr_result)==2*n:
            result.append("".join(curr_result))
            return
        if open_used<n:
            curr_result.append(parnthesis[0])
            open_used+=1
            helper(n,curr_result,open_used,closed_used)
            curr_result.pop(-1)
            open_used-=1
        if closed_used<open_used:
            curr_result.append(parnthesis[1])
            closed_used+=1
            helper(n,curr_result,open_used,closed_used)
            curr_result.pop(-1)
            closed_used-=1
    helper(n,[],0,0)
    return result

print(vp(3))
        
        
        