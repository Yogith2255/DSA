class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans=[]
        hashmap={}
        for i in strs:
            a="".join(sorted(i))
            if a in hashmap:
                hashmap[a].append(i)
            else:
                hashmap[a]=[i]
        
        for i in hashmap:
            ans.append(hashmap[i])
        return(ans)
        