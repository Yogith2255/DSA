class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        arr=[]
        for i in nums:
            for j in range(i[0],i[1]+1):
                arr.append(j)

        arr1=set(arr)
        arr=list(arr1)
        return(len(arr))
        