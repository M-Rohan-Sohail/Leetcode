class Solution(object):
    def dailyTemperatures(self, temps):
        n=len(temps)
        stack=[]
        days=[0]*n
        for i in range(n):
            while stack and temps[i]>temps[stack[-1]]:
                popped=stack.pop()
                days[popped]=i-popped
            stack.append(i) 
        return days

