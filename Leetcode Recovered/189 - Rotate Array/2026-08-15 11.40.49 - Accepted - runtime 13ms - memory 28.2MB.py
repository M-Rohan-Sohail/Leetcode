class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        if n==0 or n==1 or k==0:
            return nums
        else:
            k=k%n
            nums[:]=nums[-k:]+nums[0:-k]
        return nums

        