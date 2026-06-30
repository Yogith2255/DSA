class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix
        self.arr=[]
        for i in range(len(self.matrix)):
            s=0
            temp=[]
            for j in range(len(self.matrix[0])):
                s=s+self.matrix[i][j]
                temp.append(s)
            self.arr.append(temp)
        print(self.arr)

        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans=0
        for i in range(row2-row1+1):
            if col1==0:
                ans=ans+self.arr[row1][col2]
            else:
                ans=ans+(self.arr[row1][col2]-self.arr[row1][col1-1])
            row1+=1
            
        return ans


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)