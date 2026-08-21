class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        maxpri = prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            maxpro = max(maxpro, maxpri - prices[i])
            maxpri = max(maxpri, prices[i])

        return maxpro
