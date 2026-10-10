def erpl(tokens):
    stack=[]
    for i in range(len(tokens)):
        if tokens[i]=="+":
            if len(stack)>1:
                pop1=stack.pop(-1)
                pop2=stack.pop(-1)
                stack.append((pop1+pop2))
                
            else:
                pass
        elif tokens[i]=="-":
            if len(stack)>1:
                pop1=stack.pop(-1)
                pop2=stack.pop(-1)
                stack.append((pop2-pop1))
            else:
                pass
        elif tokens[i]=="/":
            if len(stack)>1:
                pop1=stack.pop(-1)
                pop2=stack.pop(-1)
                stack.append(int(pop2/pop1))
            else:
                pass
        elif tokens[i]=="*":
            if len(stack)>1:
                pop1=stack.pop(-1)
                pop2=stack.pop(-1)
                stack.append((pop1*pop2))
            else:
                pass
        else:
            stack.append(int(tokens[i]))
    return stack[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(erpl(tokens))
