class Solution(object):
    def romanToInt(self, nums):
        sum=0
        n=len(nums)
        key_val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(n):
            if nums[i] in key_val:
                if i+1<n and key_val[nums[i]]<key_val[nums[i+1]]:
                    sum-=key_val[nums[i]]
                else:
                    sum+=key_val[nums[i]]
        return sum
            