class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        m=0
        ans=0
        for i in hashmap:
            if hashmap[i]>m:
                m=hashmap[i]
                ans=i
        return(ans)
        