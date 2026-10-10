class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        product=1
        product_array=[1]*n
    
        # Left → Right
        for i in range(n):
            product_array[i] *= product
            product *= nums[i]
    
        # Right → Left
        product=1
        for i in range(n-1,-1,-1):
            product_array[i] *= product
            product *= nums[i]
    
        return product_array 