class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(key=lambda x:x[0],reverse=True)
        pos_spe=[]
        stack=[]
        for car in cars:
            position=car[0]
            speed=car[1]
            time=(target-position)/speed
            pos_spe.append(time)
        for time in pos_spe:
            if len(stack)==0:
                stack.append(time)
            elif time>stack[-1] :
                stack.append(time)
        return len(stack)
