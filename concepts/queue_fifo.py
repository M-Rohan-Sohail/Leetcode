class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def enqueue(self,num):
        self.queue.append(num)

    def dequeue(self):
        if len(self.queue)==0:
            print("Deqeue from Empty Queue")
            return
        else:
            self.queue.pop(0)
            return

    def front(self):
        if len(self.queue)==0:
            print("Peek from Empty Queue")
            return
        else:
            return self.queue[0]

    def rear(self):
        if len(self.queue)==0:
            print("Rear from Empty Queue")
            return
        else:
            return self.queue[-1]

    def size(self):
        return len(self.queue)

queue=Queue()
queue.enqueue(5)
queue.enqueue(15)
queue.enqueue(50)
print(queue.size())
print(queue.rear())
print(queue.front())
queue.dequeue()
print(queue.rear())
print(queue.front())
print(queue.size())

        