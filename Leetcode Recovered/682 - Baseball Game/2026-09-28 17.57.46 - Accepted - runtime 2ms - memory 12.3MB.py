class Solution(object):
    def calPoints(self, operations):
        score=[]
        for i in range(len(operations)):
            if len(score)>0 and operations[i]=="C":
                score.pop(-1)
            elif len(score)>0 and operations[i]=="D":
                score.append((score[-1])*2)
            elif len(score)>0 and operations[i]=="+":
                score.append(score[-1]+score[-2])
            else:
                try:
                    score.append(int(operations[i]))
                except ValueError:
                    pass
        return sum(score)