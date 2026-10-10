class Solution(object):
    def setZeroes(self, array):
        rows=len(array)
        cols=len(array[0])
        frz=False
        fcz=False
        for j in range(cols):
            if array[0][j]==0:
                frz=True
        for i in range(rows):
            if array[i][0]==0:
                fcz=True
        for i in range(rows):
            for j in range(cols):
                if array[i][j]==0:
                    array[0][j]=0
                    array[i][0]=0
        for z in range(1,cols):
            if array[0][z]==0:
                for i in range(rows):
                    array[i][z]=0
        for p in range(1,rows):
            if array[p][0]==0:
                for j in range(cols):
                    array[p][j]=0
        if frz:
            for j in range(cols):
                array[0][j]=0
        if fcz:
            for i in range(rows):
                array[i][0]=0

        return array