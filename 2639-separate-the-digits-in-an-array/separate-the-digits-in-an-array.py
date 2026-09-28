class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in nums:
            digits = list(map(int, str(i)))
            ans.extend(digits)
        return ans