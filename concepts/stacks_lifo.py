class Stack:
    def __init__(self):
        self.stack=[]

    def is_empty(self):
        return len(self.stack)==0

    def push(self,num):
        self.stack.append(num)

    def pop(self):
        if len(self.stack)==0:
            print("Can't Pop, Stack is Empty!")
            return
        else:
            self.stack.pop(-1)
            return

    def top(self):
        if len(self.stack)==0:
            return "Stack is Empty!"

        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

stack=Stack()

stack.push(5)
stack.push(10)
stack.push(-1)
print(stack.top())
stack.pop()
print(stack.top())
print(stack.size())