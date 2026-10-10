from collections import deque

lst=deque([])

lst.append(100)
lst.append(200)
lst.append(500)
lst.append(1000)
print(lst)
lst.appendleft(150)
print(lst)
lst.popleft()
lst.popleft()
print(lst)
lst.pop()
print(lst)
lst.reverse()
print(lst)
print(lst)