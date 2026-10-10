def ac(g,s):
    output=0
    i=0
    j=0
    g.sort()
    s.sort()
    while i!=len(g) and j!=len(s):
        if g[i]<=s[j]:
            output+=1
            i+=1
            j+=1
        else:
            j+=1
    return output

g = [1,2,3]
s = [1,1]
print(ac(g,s))