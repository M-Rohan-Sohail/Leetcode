class Solution(object):
    def grayCode(self, n):
        graycode=[0]
        for i in range(n):
            reverse=graycode[::-1]
            for k in range(len(reverse)):
                graycode.append(reverse[k]^(1<<(i)))
        return graycode