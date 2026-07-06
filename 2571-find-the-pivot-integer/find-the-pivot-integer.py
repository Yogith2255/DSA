class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        suffix=[]
        c=0
        for i in arr:
            c+=i
            suffix.append(c)
        c=0
        rev=[]
        for i in arr[::-1]:
            c+=i
            rev.append(c)
        prefix=rev[::-1]
        for i in range(len(suffix)):
            if prefix[i]==suffix[i]:
                return i+1
        return -1

        