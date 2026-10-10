class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a=0
        for i in str(x):
            a+=int(i)
        if x%a==0:
            return a
        return -1