class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        tot = 0
        count = 0
        for ele in nums:
            tot += ele
            if(tot == k):
                count += 1
            if(tot - k in mp):
                count += mp[tot-k]
            if(tot in mp):
                mp[tot] += 1
            else:
                mp[tot] = 1

        return count