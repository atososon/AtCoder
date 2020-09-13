s = int(input())
dp = [0] * (2000+1)
dp[0] = 1
dp[3] = 1
m = 10**9+7
for i in range(4, s+1):
    ans = 0
    for j in range(3, i+1):
        ans = (ans + dp[i-j]) % m
    dp[i] = ans
print(dp[s])