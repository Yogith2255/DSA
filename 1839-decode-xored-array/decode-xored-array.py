class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr=[]
        arr.append(first)
        for i in encoded:
            arr.append(arr[-1]^i)
        return(arr)
        