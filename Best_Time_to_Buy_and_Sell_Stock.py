class Solution(object):
 
            








    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_data = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[i] < prices[j]:
        #             check =  prices[j] - prices[i] 
        #             max_data = max(max_data,check)
        # return(max_data)
        # buy = prices[0]
        # this is a order of n aproche
        max_data = 0
        buy = prices[0]
        for i in range(len(prices)):
            buy = min(buy,prices[i])
            data =  prices[i] - buy 
            max_data = max(max_data,data)
        print(max_data)


    




prices = [7,1,5,3,6,4]
Solution().maxProfit(prices)