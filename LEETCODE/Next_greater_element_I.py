def ngeI(nums1,nums2):
    result={}
    final_result=[]
    stack=[]
    for num in nums2:
        while len(stack)!=0 and num>stack[-1]:
            result[stack[-1]]=num
            stack.pop()
        stack.append(num)
    for num in nums1:
        if num not in result:
            final_result.append(-1)
        else:
            final_result.append(result[num])
    return final_result

nums1 = [4,1,2] 
nums2 = [1,3,4,2]
print(ngeI(nums1,nums2))

        

            
