class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum=0
        min = True
        for i in range(1,len(prices)):
            # print(sum)
            # print(min, '  ',prices[i])
            if min:
                if prices[i]>prices[i-1]:
                    sum -=prices[i-1]
                    min = False
            else:
                if prices[i]<prices[i-1]:
                    sum +=prices[i-1]
                    min = True
        if not min:
            sum += prices[len(prices)-1]
        return max(sum,0)