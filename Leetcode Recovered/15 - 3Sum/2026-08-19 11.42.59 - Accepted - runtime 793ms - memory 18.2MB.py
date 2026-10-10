class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        nums.sort()
        triplets=[]
        if n<3:
            return []
        elif n==3:
            if nums[0]+nums[1]+nums[2]==0:
                return [nums]
            else:
                return []
        else:
            i=0
            j=i+1
            k=n-1
            while i<n-2:
                while i+1<n and nums[i+1]==nums[i] :
                    i+=1
                else:
                    while j<k:
                        if nums[i]+nums[j]+nums[k]>0:
                            k-=1
                        elif nums[i]+nums[j]+nums[k]<0:
                            j+=1
                        else:
                            triplets.append([nums[i],nums[j],nums[k]])
                            while  j<k and nums[j+1]==nums[j] :
                                j+=1
                            while  k>j and nums[k-1]==nums[k] :
                                k-=1
                            j+=1
                            k-=1
                    i+=1
                    j=i+1
                    k=n-1
            return triplets
    