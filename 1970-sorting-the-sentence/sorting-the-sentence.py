class Solution:
    def sortSentence(self, s: str) -> str:
        arr=s.split(" ")
        hashmap={}
        for i in arr: 
            if int(i[-1]) not in hashmap:
                hashmap[int(i[-1])]=i[:len(i)-1]
        print(hashmap) 
        ans=""
        for i in range(1,len(arr)+1):
            ans=ans+hashmap[i]+" "
        return ans[:len(ans)-1]