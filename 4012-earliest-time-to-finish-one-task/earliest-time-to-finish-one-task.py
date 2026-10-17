class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans=[]
        for i in tasks:
            ans.append(sum(i))
        return min(ans)