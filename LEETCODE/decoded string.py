def decoded_string(string):
    stack=[]
    current=""
    integer=0
    for i in range(len(string)):
        if string[i].isdigit():
            integer=(integer*10)+int(string[i])
        elif string[i]=="[":
            stack.append((integer,current))
            current=""
            integer=0
        elif string[i].isalpha():
            current+=string[i]
        else:
            pop1=stack.pop(-1)
            current=pop1[1]+(pop1[0]*current)
    return current

string="3[a2[c]]"
print(decoded_string(string))

