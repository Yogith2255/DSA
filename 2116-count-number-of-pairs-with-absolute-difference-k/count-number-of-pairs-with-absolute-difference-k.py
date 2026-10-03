class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        c=0
        hashmap={}
        for i in nums:
            if i-k in hashmap:
                c+=hashmap[i-k]
            if i+k in hashmap:
                c+=hashmap[i+k]
            hashmap[i]=hashmap.get(i,0)+1
        return c