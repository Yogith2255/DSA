class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        arr=[]
        for i in ranges:
            for j in range(i[0],i[1]+1):
                arr.append(j)
        print(arr)
        for i in range(left,right+1):
            if i not in arr:
                return False
        return True
        