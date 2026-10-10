class Solution(object):
    def maxScore(self, cardPoints, k):
            original_k=k
            wall=cardPoints[:k]
            curr_sum=sum(wall)
            maxx=sum(wall)
            i=1
            while k!=0:
                removed=wall.pop(original_k-i)
                added=cardPoints[-i]
                wall.append(added)
                curr_sum=curr_sum-removed+added
                maxx=max(maxx,curr_sum)
                k-=1
                i+=1
            return maxx