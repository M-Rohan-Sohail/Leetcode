class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result=[]
        curr_result=[]
        def helper(index):
            i=0
            if len(curr_result)==4:
                if index==len(s):
                    result.append(".".join(curr_result))
                    return
            for length in range(1,4):
                if length+index>len(s):
                    break
                pick=s[index:index+length]
                if int(pick)>255:
                    continue
                if len(pick)>1 and pick[0]=="0":
                    continue
                curr_result.append(pick)
                helper(index+length)
                curr_result.pop()
        helper(0)
        return result
