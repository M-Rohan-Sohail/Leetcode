class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        postive_numbers=[]
        negtive_numbers=[]
        arranged_array=[]
        for x in range(n):
            if nums[x]>=0:
                postive_numbers.append(nums[x])
            else:
                negtive_numbers.append(nums[x])
        i,j=0,0
        while i<len(postive_numbers) and j<len(negtive_numbers):
            arranged_array.append(postive_numbers[i])
            arranged_array.append(negtive_numbers[j])
            i+=1
            j+=1
        if i<len(postive_numbers):
            while i<len(postive_numbers):
                arranged_array.append(postive_numbers[i])
                i+=1
        if j<len(negtive_numbers):
            while j<len(negtive_numbers):
                arranged_array.append(negtive_numbers[j])
                j+=1
        return arranged_array