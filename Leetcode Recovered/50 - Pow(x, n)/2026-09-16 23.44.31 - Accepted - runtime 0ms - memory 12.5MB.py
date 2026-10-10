class Solution(object):
    def myPow(self, x, n):
            if n<0:
                x=1/x
                n=(-n)
            if n==0:
                return 1
            elif n%2==0:
                    half=pow(x,n//2)
                    return (half*half)
            elif n%2!=0:
                    half=pow(x,n//2)
                    return (half*half*x)