class Solution(object):
    def isPalindrome(self, x):
        xy=str(x)
        if xy==xy[::-1]:
            return True
        else:
            return False
        