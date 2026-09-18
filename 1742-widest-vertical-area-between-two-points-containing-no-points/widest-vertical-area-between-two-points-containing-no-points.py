class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        arr=[]
        for i in points:
            arr.append(i[0])
        arr.sort()
        if len(arr)==2:
            return abs(arr[0]-arr[1])
        ans=[]
        for i in range(len(arr)-2):
            ans.append(abs(arr[i]-arr[i+1]))
        return max(ans)