class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        tp=0
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
            tp=max(tp,prices[r]-prices[l])  
            r+=1
        return tp