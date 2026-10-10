class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix[0])
        low=0
        high=(len(matrix)*len(matrix[0]))-1
        while low<=high:
              mid=(low+high)//2
              row=mid//n
              col=mid%n
              if matrix[row][col]==target:
                    return True
              elif matrix[row][col]<target:
                    low=mid+1
              else:
                    high=mid-1
        return False
