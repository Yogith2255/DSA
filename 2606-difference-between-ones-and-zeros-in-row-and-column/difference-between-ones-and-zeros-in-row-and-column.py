class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m=len(grid)
        n=len(grid[0])
        row_ones=[]
        row_zeros=[]
        col_ones=[]
        col_zeros=[]
        for i in grid:
            row_ones.append(i.count(1))
            row_zeros.append(i.count(0))
        print(row_ones)
        print(row_zeros)
        for i in range(n):
            o=0
            z=0
            for j in range(m):
                if grid[j][i]==0:
                    z+=1
                else:
                    o+=1
            col_ones.append(o)
            col_zeros.append(z)
        print(col_ones)
        print(col_zeros)
        ans=[]
        for i in range(m):
            arr=[]
            for j in range(n):
                diff=row_ones[i]+col_ones[j]-row_zeros[i]-col_zeros[j]
                arr.append(diff)
            ans.append(arr)
        return(ans)
