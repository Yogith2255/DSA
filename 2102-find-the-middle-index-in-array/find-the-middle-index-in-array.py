class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        print(prefix)
        c=0
        ending=[0]
        for i in nums[::-1]:
            c=c+i
            ending.append(c)
        suffix=ending[::-1]
        print(suffix)
        for i in range(0,len(prefix)-1):
            if prefix[i]==suffix[i+1]:
                return i
        return -1
        