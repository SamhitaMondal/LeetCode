class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        dp = [0] * (budget + 1)

        min_price = float('inf')

        for i in range(n):

            factor, price = items[i]

            min_price = min(min_price, price)

            # Count purchased + free items
            cnt = 0

            for j in range(n):
                if items[j][0] % factor == 0:
                    cnt += 1

            # 0/1 Knapsack
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + cnt)

        ans = 0

        for i in range(budget + 1):
            extra = (budget - i) // min_price

            ans = max(ans, dp[i] + extra)

        return ans
        