n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

dp = [0 for _ in range(10001)]
for coin in coins:
    dp[coin] = 1

for i in range(coins[0], m+1):
    for coin in coins:
        if i - coin < 0:
            continue
        
        dp[i] = max(dp[i], dp[i-coin] + 1)

ans = -1 if dp[m] == 0 else dp[m]
print(ans)