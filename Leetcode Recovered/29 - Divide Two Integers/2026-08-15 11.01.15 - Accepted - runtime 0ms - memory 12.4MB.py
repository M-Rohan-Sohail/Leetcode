class Solution(object):
    def divide(self, div, divs):
        count=0
        negative= (div<0) != (divs<0)
        div=abs(div)
        divs=abs(divs)
        MAX_INT = 2147483647  # 2^31 - 1
        MIN_INT = -2147483648 # -2^31
        while div>=divs:
            temp=divs
            multiple=1
            while div>=temp+temp:
                temp+=temp
                multiple+=multiple
            div-=temp
            count+=multiple
        if negative:
            count=-count
        if count>MAX_INT:
            return MAX_INT
        if count < MIN_INT:
            return MIN_INT
        return count
            