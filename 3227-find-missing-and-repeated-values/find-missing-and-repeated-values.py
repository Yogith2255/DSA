class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr=[]
        for i in grid:
            arr.extend(i)
        ans=[]
        for i in arr:
            if arr.count(i)==2:
                ans.append(i)
                break
        print(ans)
        for i in range(1,max(arr)+1):
            if i not in arr:
                ans.append(i)
                break
        if len(ans)==1:
            ans.append(max(arr)+1)
        return ans



