class Solution(object):
    def singleNumber(self, nums):
                answer=0
                for i in range(32):
                    count=0
                    for num in nums:
                        curr_bit=(num>>i)&1
                        if curr_bit==1:
                            count+=1
                    if count%3==1:
                        answer=answer|1<<i
                if answer>=(1<<31):
                    answer=~(answer^0xFFFFFFFF)
                return answer
            
            
                            