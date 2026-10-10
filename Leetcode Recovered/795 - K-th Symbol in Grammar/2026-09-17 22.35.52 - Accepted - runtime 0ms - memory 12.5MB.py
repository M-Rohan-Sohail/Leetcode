class Solution(object):
    def kthGrammar(self, n, k):
        if n==1:
            return 0
        parent=(k+1)//2
        result=self.kthGrammar(n-1,parent)
        if result%2==0:
            if k%2==0:
                return 1
            else:
                return 0    
        else:
            if k%2==0:
                return 0
            else:
                return 1