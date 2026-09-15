class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ts=0
        arr=[]
        for i in bank:
            if i.count('1'):
                arr.append(i.count('1'))
            if len(arr)==2:
                ts+=arr[0]*arr[1]
                arr.pop(0)
        return(ts)
        