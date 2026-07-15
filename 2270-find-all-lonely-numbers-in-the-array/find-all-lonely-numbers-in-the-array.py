class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        ans=[]
        for i in hashmap:
            if hashmap[i]==1 and i-1 not in hashmap and i+1 not in hashmap:
                ans.append(i)
        return ans