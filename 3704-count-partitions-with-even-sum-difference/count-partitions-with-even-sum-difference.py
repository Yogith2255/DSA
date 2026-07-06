class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        s=sum(nums)
        c=0
        for i in range(len(nums)-1):
            c=c+nums[i]
            if abs(c-(s-c))%2==0:
                print(c,(s-c))
                ans+=1
        
        return ans
        