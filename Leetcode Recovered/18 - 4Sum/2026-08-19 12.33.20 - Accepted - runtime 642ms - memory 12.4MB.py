class Solution(object):
    def fourSum(self, nums, target):
        n=len(nums)
        nums.sort()
        quadruplets=[]
        if n<4:
            return []
        else:
            i=0
            j=i+1
            k=j+1
            l=n-1
            while i<n-3:
                while i<n-3 and nums[i+1]==nums[i]:
                    i+=1
                while j<n-2:
                    while j+1<n and nums[j+1]==nums[j]:
                        j+=1
                    else:
                        while k<l:
                            if nums[i]+nums[j]+nums[k]+nums[l]>target:
                                l-=1
                            elif nums[i]+nums[j]+nums[k]+nums[l]<target:
                                k+=1
                            else:
                                quadruplets.append([nums[i],nums[j],nums[k],nums[l]])
                                while k<l and nums[k+1]==nums[k]:
                                    k+=1
                                while l<k and nums[l-1]==nums[l]:
                                    l-=1
                                k+=1
                                l-=1
                        j+=1
                        k=j+1
                        l=n-1
                i+=1
                j=i+1
                k=j+1
                l=n-1
            return quadruplets