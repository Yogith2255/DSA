class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=[]
        c=0
        ans=0
        for i in nums:
            c+=i
            if c==0:
                ans+=1
        return ans
        