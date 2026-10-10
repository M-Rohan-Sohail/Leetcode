class Solution(object):
    def spiralOrder(self, nums):
        rows=len(nums)
        cols=len(nums[0])
        unique=[]
        top=0
        bottom=rows-1
        left=0
        right=cols-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                unique.append(nums[top][i])
            top+=1
            if top<=bottom:
                for j in range(top,bottom+1):
                    unique.append(nums[j][right])
                right-=1
            if top <=bottom:
                for k in range(right,left-1,-1):
                    unique.append(nums[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    unique.append(nums[l][left])
                left+=1
        return unique
    
            