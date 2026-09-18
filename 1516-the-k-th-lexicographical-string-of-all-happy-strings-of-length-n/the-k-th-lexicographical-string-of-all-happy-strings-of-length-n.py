class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans=[]
        cur=[-1]
        letters=['a','b','c']
        def recur(ans,cur,letters,n):
            if len(cur)==n+1:
                ans.append(cur.copy())
                # print(ans)
                return
            for i in letters:
                if cur[-1]!=i:
                    cur.append(i)
                    recur(ans,cur,letters,n)
                    cur.pop()




        recur(ans,cur,letters,n)
        if len(ans) >=k:
            return("".join(ans[k-1][1:]))
        else:
            return("")
        