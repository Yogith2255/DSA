class Solution:
    def minimumSum(self, num: int) -> int:
        arr=[]
        for i in str(num):
            if i !="0":
                arr.append(int(i))
        nums1=""
        nums2=""
        arr.sort()
        for i in range(len(arr)):
            if i%2==0:
                nums1+=str(arr[i])
            else:
                nums2+=str(arr[i])
        s=0
        if nums1:
            s+=int(nums1)
        if nums2:
            s+=int(nums2)
        return(s)
        