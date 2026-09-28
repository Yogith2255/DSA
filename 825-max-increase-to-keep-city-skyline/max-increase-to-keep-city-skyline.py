class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        rows=[]
        cols=[]
        n=len(grid)
        for i in grid:
            rows.append(max(i))
        for i in range(n):
            arr=[]
            for j in range(n):
                arr.append(grid[j][i])
            cols.append(max(arr))
        s=0
        for i in range(n):
            for j in range(n):
                m=min(rows[i],cols[j])
                s=s+(m-grid[i][j])
        return s
        