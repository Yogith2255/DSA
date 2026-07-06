class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        arr=[]
        for i in s:
            arr.append(alpha.index(i)+1)
        prefix=[]
        c=0
        for i in arr:
            c+=i
            prefix.append(c)
        print(prefix)
        rev=[]
        c=0
        for i in arr[::-1]:
            c+=i
            rev.append(c)
        suffix=rev[::-1]
        print(suffix)
        for i in range(len(prefix)-1):
            if prefix[i]==suffix[i+1]:
                return True
        return False
