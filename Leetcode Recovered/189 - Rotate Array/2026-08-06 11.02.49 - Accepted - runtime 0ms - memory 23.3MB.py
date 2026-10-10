class Solution(object):
    def rotate(self, nums, k):
      n=len(nums)
      if n==1 or k==0:
            return nums
      k=k%n
      nums[:]=nums[-k:]+nums[0:-k]
      return nums
        