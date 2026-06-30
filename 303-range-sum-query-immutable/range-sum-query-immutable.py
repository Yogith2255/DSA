class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.arr=[]
        s=0
        for i in self.nums:
            s=s+i
            self.arr.append(s)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left==0:
            return self.arr[right]
        return(self.arr[right]-self.arr[left-1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)