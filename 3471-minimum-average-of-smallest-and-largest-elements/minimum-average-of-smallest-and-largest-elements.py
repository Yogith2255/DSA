class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        for i in range(len(nums)//2):
            ma=max(nums)
            mi=min(nums)
            avg.append((ma+mi)/2)
            nums.pop(nums.index(ma))
            nums.pop(nums.index(mi))
        return min(avg)