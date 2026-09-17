class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lc=[]
        rc=[]
        lis=[]
        ris=[]
        lc.append(int(boxes[0]))
        for i in range(1,len(boxes)):
            lc.append(int(boxes[i])+lc[-1])
        print(lc)
        rc.append(int(boxes[len(boxes)-1]))
        for i in range(len(boxes)-2,-1,-1):
            rc.append(int(boxes[i])+rc[-1])
        rc=rc[::-1]
        print(rc)
        print("--------------------")
        lis.append(0)
        for i in range(1,len(boxes)):
            lis.append(lis[-1] + i*int(boxes[i]))
        print(lis)
        ris.append((len(boxes)-1)*int(boxes[len(boxes)-1]))
        for i in range(len(boxes)-2,-1,-1):
            ris.append(ris[-1] + i*int(boxes[i]))
        ris=ris[::-1]
        print(ris)

        ans=[]
        for i in range(len(boxes)):
            s=0
            if i>0 and lc[i-1] !=0:
                s+=(i*lc[i-1])-(lis[i-1])
            if i<len(boxes)-1 and rc[i+1]!=0:
                s+=(ris[i+1])-(i*rc[i+1])
            ans.append(s)
        return(ans)
        