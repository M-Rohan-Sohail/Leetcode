class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        postive_numbers=[]
        negtive_numbers=[]
        for x in range(n):
            if nums[x]>=0:
                postive_numbers.append(nums[x])
            else:
                negtive_numbers.append(nums[x])
        i,j=0,0
        o,p=0,1
        while i<len(postive_numbers) and j<len(negtive_numbers) and o<n and p<n:
            nums[o]=postive_numbers[i]
            nums[p]=negtive_numbers[j]
            i+=1
            j+=1
            o+=2
            p+=2
        return nums