class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            s=0
            for j in str(i):
                s+=int(j)
            ans.append(s)
        return min(ans)