def oss(prices):
    result=[]
    for price in prices:
        span=1
        while result and result[-1][0]<=price:
            span=span+result[-1][1]
            result.pop(-1)
        result.append((price,span))
    return result
    
prices=[[50],[98],[54],[6],[34]]
print(oss(prices))
     