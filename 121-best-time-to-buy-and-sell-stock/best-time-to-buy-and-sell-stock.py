class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum=prices[0]
        profit=0
        for i in prices:
            minimum=min(minimum,i)
            profit=max(profit,i-minimum)
        return profit