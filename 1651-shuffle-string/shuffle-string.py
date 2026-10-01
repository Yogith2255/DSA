class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        ans=""
        m=max(indices)
        for i in range(m+1):
            ans+=s[indices.index(i)]
        return(ans)