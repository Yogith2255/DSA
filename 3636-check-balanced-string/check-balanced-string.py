class Solution:
    def isBalanced(self, num: str) -> bool:
        o=0
        e=0
        for i in range(len(num)):
            if i%2==0:
                e+=int(num[i])
            else:
                o+=int(num[i])
        print(o,e)
        return o==e