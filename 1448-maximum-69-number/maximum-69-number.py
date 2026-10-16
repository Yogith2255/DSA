class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        ma=num
        for i in range(len(n)):
            if n[i]=="6":
                cn=n[:i]+"9"+n[i+1:]
                ma=max(int(cn),ma)
            else:
                cn=n[:i]+"6"+n[i+1:]
                ma=max(int(cn),ma)
        return ma