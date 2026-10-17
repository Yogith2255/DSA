class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        arr=s.split(":")
        print(arr)
        ans=[]
        alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        if arr[0][-1]==arr[1][-1]:
            s=alp.index(arr[0][0])
            e=alp.index(arr[1][0])
            for i in range(s,e+1):
                ans.append(alp[i]+arr[0][-1])
        else:
            s=alp.index(arr[0][0])
            e=alp.index(arr[1][0])
            for i in range(s,e+1):
                for j in range(int(arr[0][-1]),int(arr[1][-1])+1):
                    ans.append(alp[i]+str(j))
        return ans