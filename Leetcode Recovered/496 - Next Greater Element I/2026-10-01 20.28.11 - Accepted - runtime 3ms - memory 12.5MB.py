class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
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
                    