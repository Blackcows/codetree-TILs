dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    if i < 5:
        dp[i] = dp[i-1] + dp[i-2]
    elif i == 5:
        dp[i] = dp[i-1] + dp[i-2] + 1
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-5]

# print(dp)

n = int(input())

ans = dp[n] % 10007
print(ans)