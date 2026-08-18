class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()

        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            minimum = float('inf')

            for coin in coins:
                difference = i - coin

                if difference < 0:
                    continue
                
                minimum = min(minimum, dp[difference] + 1)
            
            dp[i] = minimum
        
        return dp[amount] if dp[amount] < float('inf') else - 1
                

