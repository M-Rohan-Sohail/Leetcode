class Solution(object):
    def isPalindrome(self, x):
        numx=str(x)
        numxx=numx[::-1]
        if numx==numxx:
            return True
        else:
            return False
        