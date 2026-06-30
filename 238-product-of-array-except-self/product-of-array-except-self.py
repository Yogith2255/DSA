class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        revnums=nums[::-1]
        prefix=[]
        suffix=[]
        p=1
        s=1
        for i in nums:
            p=p*i
            prefix.append(p)
        for i in revnums:
            s=s*i
            suffix.append(s)

        sufix=suffix[::-1]
        ans=[]
        for i in range(len(nums)):
            if i==0:
                ans.append(sufix[i+1])
            elif i==len(nums)-1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1]*sufix[i+1])
        return(ans)
        