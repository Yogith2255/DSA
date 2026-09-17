class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans=[]
        hashmap={}
        ind=0
        for i in groupSizes:
            if i in hashmap:
                if len(hashmap[i])<i:
                    hashmap[i].append(ind)
                    ind+=1
                else:
                    ans.append(hashmap[i])
                    hashmap[i]=[ind]
                    ind+=1
            else:
                hashmap[i]=[ind]
                ind+=1
        for i in hashmap:
            ans.append(hashmap[i])
        ans.sort(key=lambda x: len(x))
        return(ans)
        