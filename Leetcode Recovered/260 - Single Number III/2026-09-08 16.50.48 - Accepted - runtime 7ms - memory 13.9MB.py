class Solution(object):
    def singleNumber(self, nums):
                start_num=nums[0]
                group1=[]
                group2=[]
                answer=[]
                for i in range(1,len(nums)):
                    start_num=start_num^nums[i]
                    xor_result=start_num
                set_bit=xor_result&(-xor_result)
                for num in nums:
                    if num&set_bit==0:
                       group1.append(num)
                    else:
                        group2.append(num)
                answer1=0
                answer2=0
                for i in range(len(group1)):
                    answer1=answer1^group1[i]
                answer.append(answer1)
                for i in range(len(group2)):
                    answer2=answer2^group2[i]
                answer.append(answer2)
                return answer

        