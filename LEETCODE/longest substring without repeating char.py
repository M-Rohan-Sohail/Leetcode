def lsswrc(s):
    substring=[]
    counts=[]
    j=0
    while j!=len(s):
        if s[j] not in substring:
            substring.append(s[j])
            count+=1
        else:
            while s[j] in substring:
                substring.pop(0)
            substring.append(s[j])
        counts.append(len(substring))
        j+=1   
    return max(counts)
s = "pwwkew"
print(lsswrc(s))



            

