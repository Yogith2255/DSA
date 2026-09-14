class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ans=s[:k][::-1]
        ans+=s[k:]
        return ans       