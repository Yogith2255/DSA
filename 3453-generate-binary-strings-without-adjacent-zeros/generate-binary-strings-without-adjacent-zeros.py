class Solution:
    def validStrings(self, n: int) -> List[str]:
        arr=[-1]
        ans=[]
        def recur(ans,arr,n):
            if len(arr)==n+1:
                ans.append("".join(arr[1:]))
                return
            if arr[-1]!="0":
                arr.append("1")
                recur(ans,arr,n)
                arr.pop()
                arr.append("0")
                recur(ans,arr,n)
                arr.pop()
                
            else:
                arr.append("1")
                recur(ans,arr,n)
                arr.pop()
        recur(ans,arr,n)
        return(ans)
        