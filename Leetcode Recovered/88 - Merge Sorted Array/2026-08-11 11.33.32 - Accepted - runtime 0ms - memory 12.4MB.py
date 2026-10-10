class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j=0,0
        unique=[]
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                unique.append(nums1[i])
                i+=1
            else:
                unique.append(nums2[j])
                j+=1
        if i<m:
            while i<m:
                unique.append(nums1[i])
                i+=1
        else:
            while j<n:
                unique.append(nums2[j])
                j+=1
        nums1[:]=unique
        return nums1
