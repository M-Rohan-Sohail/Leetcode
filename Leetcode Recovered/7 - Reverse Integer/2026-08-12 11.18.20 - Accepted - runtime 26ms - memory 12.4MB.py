class Solution(object):
    def reverse(self, x):
        nums=x
        result=0
        while nums!=0:
            last=nums%10
            if nums<0 and last>0:
                last-=10
            nums=int(float(nums)/10)
            if result > 214748364 or (result == 214748364 and last > 7):
                return 0
            if result < -214748364 or (result == -214748364 and last < -8):
                return 0
            result=(result*10)+last
        return result

        