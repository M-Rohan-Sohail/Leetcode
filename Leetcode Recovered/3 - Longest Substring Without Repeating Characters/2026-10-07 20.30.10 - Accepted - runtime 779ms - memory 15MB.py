class Solution(object):
    def lengthOfLongestSubstring(self, s):
            substring=[]
            counts=[]
            j=0
            if len(s)==0:
                return 0
            else:    
                while j!=len(s):
                    if s[j] not in substring:
                        substring.append(s[j])
                    else:
                        while s[j] in substring:
                            substring.pop(0)
                        substring.append(s[j])
                    counts.append(len(substring))
                    j+=1   
                return max(counts)
    