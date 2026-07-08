class Solution(object):
    def search(self, nums, target):
        def binary(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(left, mid - 1)
            else:
                return binary(mid + 1, right)
        return binary(0, len(nums) - 1)