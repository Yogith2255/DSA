class Solution:
    def balancedStringSplit(self, s: str) -> int:
        hashmap={'L':0,'R':0}
        ans=0
        for i in s:
            hashmap[i]+=1
            if hashmap["L"]==hashmap['R']:
                ans+=1
                hashmap['L']=0
                hashmap['R']=0

        return ans