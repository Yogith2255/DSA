class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        ans=[]
        for x in range(l,r+1):
            for i in range(len(nums)-x+1):
                if sum(nums[i:i+x])>0:
                    ans.append(sum(nums[i:i+x]))
        
        if ans:
            print(ans)
            return(min(ans))
        return -1