class Solution(object):
    def totalFruit(self, fruits):
        count=[]
        i=0
        max_count=0
        freq={}
        while i!=len(fruits):
            if fruits[i] not in freq:
                freq[fruits[i]] = 1
            else:
                freq[fruits[i]] += 1
            if len(freq)<=2:
                count.append(fruits[i])
            else:
                while len(freq)>2:
                    removed=count.pop(0)
                    freq[removed]-=1
                    if freq[removed]==0:
                        del freq[removed]
                count.append(fruits[i])
            i+=1
            max_count=max(max_count,len(count))
        return max_count
