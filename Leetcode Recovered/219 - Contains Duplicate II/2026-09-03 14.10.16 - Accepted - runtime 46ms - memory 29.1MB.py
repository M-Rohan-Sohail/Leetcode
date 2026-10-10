class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_scene = {}
        i = 0
        
        for num in nums:
            if num in last_scene:
                if i - last_scene[num] <= k:
                    return True
                else:
                    last_scene[num] = i
            else:
                last_scene[num] = i
        
            i += 1
        
        return False
        
        