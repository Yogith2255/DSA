class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num1<100 and num2<100:
            return 0
        if num1<100:
            num1=100
        c=0
        for i in range(num1,num2+1):
            s=int(str(i)[0])
            e=int(str(i)[len(str(i))-1])
            for j in range(1, len(str(i))-1):
                if (int(str(i)[j]) > int(str(i)[j-1]) and int(str(i)[j]) > int(str(i)[j+1])) or (int(str(i)[j]) < int(str(i)[j-1]) and int(str(i)[j]) < int(str(i)[j+1])):
                    c+=1
        return c
        