class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        unique=[]
        for num in nums:
            if num not in unique:
                unique.append(num)
        low=0
        high=len(unique)-1
        while low<=high:
            mid=(low+high)//2
            if unique[mid]==target:
                return True
            elif unique[low]<=unique[mid]:
                if unique[low]<=target<=unique[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if unique[mid]<=target<=unique[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
    