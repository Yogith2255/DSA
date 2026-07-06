class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[]
        for i in s:
            arr.append(int(i))
        zeros=[]
        one=[]
        c=0
        for i in arr:
            if i==0:
                c=c+1
            zeros.append(c)
        c=0
        for i in arr[::-1]:
            if i==1:
                c=c+1
            one.append(c)
        ones=one[::-1]
        print(zeros)
        print(ones)
        m=-1
        for i in range(1,len(arr)):
            if zeros[i-1]+ones[i]>m:
                m=zeros[i-1]+ones[i]
        return(m)
        