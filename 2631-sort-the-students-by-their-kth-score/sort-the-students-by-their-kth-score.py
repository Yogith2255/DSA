class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        hashmap={}
        for i in score:
            hashmap[i[k]]=i
        print(hashmap)
        ans=[]
        arr=list(hashmap.keys())
        arr.sort()
        arr=arr[::-1]
        print(arr)
        for i in arr:
            ans.append(hashmap[i])
        return ans

        