from collections import deque
class StackUsingQueue:
    def __init__(self):
            self.queue=deque()
    def push(self,items):
          self.queue.append(items)
          for _ in range(len(self.queue)-1):
                self.queue.append(self.queue.popleft())
    def pop(self):
          if len(self.queue)==0:
                return "Stack is Empty!"
          return self.queue.popleft()
    def peek(self):
          if len(self.queue)==0:
                return "Stack is Empty!"
          return self.queue[0]
    def is_empty(self):
          return len(self.queue)==0
    def size(self):
          return len(self.queue)

suq=StackUsingQueue()

suq.push(10)
suq.push(5)
suq.push(15)
print(suq.peek())
print(suq.size())
suq.pop()
print(suq.peek())
print(suq.size())
suq.pop()
print(suq.peek())
print(suq.size())