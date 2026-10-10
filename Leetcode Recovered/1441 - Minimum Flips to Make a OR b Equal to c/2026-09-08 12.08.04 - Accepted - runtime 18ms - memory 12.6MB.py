class Solution(object):
    def minFlips(self, a, b, c):
            biggest_num=max(a,b,c)
            count=0
            if a|b==c:
                return count
            else:
                for i in range(biggest_num.bit_length()):
                    a_bit=(a>>i)&1
                    b_bit=(b>>i)&1
                    c_bit=(c>>i)&1
                    if c_bit==0:
                        if (a_bit==0 and b_bit==1) or (a_bit==1 and b_bit==0):
                            count+=1
                        elif a_bit==1 and b_bit==1:
                            count+=2
                        else:
                            count+=0
                    elif c_bit==1:
                        if a_bit==0 and b_bit==0:
                            count+=1
                        else:
                            count+=0
                return count