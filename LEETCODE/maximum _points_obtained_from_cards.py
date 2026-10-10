def maxpoints(cards,k):
    original_k=k
    wall=cards[:k]
    curr_sum=sum(wall)
    maxx=sum(wall)
    i=1
    while k!=0:
        removed=wall.pop(original_k-i)
        added=cards[-i]
        wall.append(added)
        curr_sum=curr_sum-removed+added
        maxx=max(maxx,curr_sum)
        k-=1
        i+=1
    return maxx

        

    

cards = [1,2,3,4,5,6,1]
k = 3
print(maxpoints(cards,k))

        


