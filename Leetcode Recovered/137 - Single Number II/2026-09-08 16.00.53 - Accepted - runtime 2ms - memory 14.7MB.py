class Solution(object):
    def singleNumber(self, nums):
                dict_x={}
                for num in nums:
                    if num not in dict_x:
                        dict_x[num]=1
                    else:
                        dict_x[num]+=1
                result=next(k for k, v in dict_x.items() if v==1)
                return result

