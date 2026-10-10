def carfleet(target,position,speed):
    cars=list(zip(position,speed))
    cars.sort(key=lambda x:x[0],reverse=True)
    pos_spe=[]
    stack=[1]
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

target = 10
position = [6,8]
speed = [3,2]
print(carfleet(target,position,speed))