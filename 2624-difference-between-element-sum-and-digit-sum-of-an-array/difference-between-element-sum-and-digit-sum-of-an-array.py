class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s=sum(nums)
        a=0
        for i in nums:
            for j in str(i):
                a+=int(j)
        return abs(s-a)