class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f=0
        for i in nums1:
            if i in nums2:
                f+=1
        s=0
        for i in nums2:
            if i in nums1:
                s+=1
        return [f,s]