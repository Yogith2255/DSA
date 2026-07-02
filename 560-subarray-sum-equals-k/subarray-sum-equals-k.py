class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixsum=0
        hashmap={0:1}
        ans=0
        for i in nums:
            prefixsum+=i
            if (prefixsum-k) in hashmap:
                ans+=hashmap[prefixsum-k]
            if prefixsum in hashmap:
                hashmap[prefixsum]+=1
            else:
                hashmap[prefixsum]=1
        return(ans)
        