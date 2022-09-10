class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        dp = [float("inf") for i in range(max(days)+1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            
            if i not in days:
                dp[i] = dp[i-1]
                continue
            
            # We have three choices
            # - Buy a one day pass
            # - Buy a seven day pass
            # - Buy a 30 day pass
            
            dp[i] = min(dp[i], dp[i-1] + costs[0])
            
            if i - 7 >= 0:
                dp[i] = min(dp[i], dp[i-7] + costs[1])
            else:
                dp[i] = min(dp[i], costs[1])
                
            if i - 30 >= 0:
                dp[i] = min(dp[i], dp[i-30] + costs[2])
            else:
                dp[i] = min(dp[i], costs[2])
                
            
            
        return dp[-1]
            
                
            
            
