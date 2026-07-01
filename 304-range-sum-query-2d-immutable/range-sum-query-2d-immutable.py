class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows=len(matrix)
        cols=len(matrix[0])

        for i in matrix:
            print(i)
        self.rectangle=[]
        for i in range(rows+1):
            s=[]
            for j in range(cols+1):
                s.append(0)
            self.rectangle.append(s)
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                self.rectangle[i][j]=self.rectangle[i-1][j]+self.rectangle[i][j-1]+matrix[i-1][j-1]-self.rectangle[i-1][j-1]

        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        return(self.rectangle[row2][col2]-self.rectangle[row1-1][col2]-self.rectangle[row2][col1-1]+self.rectangle[row1-1][col1-1])
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)