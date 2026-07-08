class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        openb=["(","{","["]
        for i in s:
            if i in openb:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i==")" and stack[-1]=="(":
                    stack.pop()
                elif i=="}" and stack[-1]=="{":
                    stack.pop()
                elif i=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True