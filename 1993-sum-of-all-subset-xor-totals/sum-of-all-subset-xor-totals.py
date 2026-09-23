class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def recur(total,ans,nums,index):
            if(index==len(nums)):
                
                total.append(ans.copy())
                return
            if index>len(nums):
                return
            ans.append(nums[index])
            recur(total,ans,nums,index+1)
            ans.pop()
            recur(total,ans,nums,index+1)
        
        total=[]
        ans=[]
        index=0
        recur(total,ans,nums,index)
        print(total)
        s=0
        for i in total:
            c=0
            for j in i:
                c=c^j
            s=s+c
        return(s)
        