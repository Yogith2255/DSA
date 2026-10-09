class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        ind=[]
        h=heights.copy()
        heights.sort()
        for i in heights[::-1]:
            ind.append(h.index(i))
        ans=[]
        for i in ind:
            ans.append(names[i])
        return ans