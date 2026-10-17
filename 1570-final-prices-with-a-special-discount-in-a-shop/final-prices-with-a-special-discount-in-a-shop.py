class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ans=[]
        for i in range(len(prices)):
            j=i+1
            a=False
            while j<len(prices):
                if prices[j]<=prices[i]:
                    a=True
                    break
                j+=1
            if a:
                ans.append(prices[i]-prices[j])
            else:
                ans.append(prices[i])
        return ans
            