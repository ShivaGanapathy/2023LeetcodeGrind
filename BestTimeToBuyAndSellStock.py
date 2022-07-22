class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """Solution 1: O(n^2) time, O(1) space"""
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = max(prices[j]-prices[i], max_profit)
                
        return max_profit
        
        """Solution 2: O(n) time, O(1) space"""
        max_profit = 0
        buy_price = prices[0]
        
        for rp in range(len(prices)):
            current_profit = prices[rp] - buy_price

            if current_profit < 0:
                current_profit = 0
                buy_price = prices[rp]
                
            max_profit = max(current_profit, max_profit)
            
        
        return max_profit
            
