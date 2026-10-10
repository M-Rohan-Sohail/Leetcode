class Solution(object):
    def getSum(self, a, b):
        MASK=0xFFFFFFFF # Filter down only 32 bits
        MAX_INT=0x7FFFFFFF # Max Int Support
        sum_wo_carry=a^b
        carry=(a&b)<<1
        while carry!=0:
                old_sum=sum_wo_carry
                sum_wo_carry=(sum_wo_carry^carry)&MASK
                carry=((old_sum&carry)<<1)&MASK
        if sum_wo_carry<=MAX_INT:
              return sum_wo_carry
        else:
              return ~(sum_wo_carry^MASK) # Convert Number to Negtive