class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ans=[]
        for i in range(len(l)):
            s=l[i]
            e=r[i]
            arr=nums[s:e+1]
            arr.sort()
            diff=arr[1]-arr[0]
            a=True
            for j in range(len(arr)-1):
                if arr[j+1]-arr[j]!=diff:
                    a=False
                    break
            ans.append(a)
        return(ans)
            