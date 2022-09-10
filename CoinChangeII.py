class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [ [0] * (amount + 1) for _ in range(len(coins)) ]
        
        # There is one way to make 0 coins
        dp[0][0] = 1
        
        
        for i in range(len(coins)):
            
            for j in range(amount + 1):
                coin = coins[i]

                # First we can add values within the same row (include)
                if j - coin >= 0:
                    dp[i][j] = dp[i][j - coin]
                    
                
                # Second we can add values if we excluded
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                    
        
        return dp[-1][-1]
                    
            
