class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        prefix=[]
        for i in nums:
            s=s+i
            prefix.append(s)
        suffix=[]
        s=0
        rev=nums[::-1]
        for i in nums[::-1]:
            s=s+i
            suffix.append(s)
        
        rev=suffix[::-1]
        for i in range(len(prefix)):
            if prefix[i]==rev[i]:
                return i
        return -1


        