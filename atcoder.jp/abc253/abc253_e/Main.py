#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, M: int, K: int):
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, M+1):
        dp[1][i] = 1
    for i in range(2, N+1):
        cum_sum = [0]*(M+1)
        for j in range(1, M+1):
            cum_sum[j] = (cum_sum[j-1] + dp[i-1][j]) % MOD
        for j in range(1, M+1):
            if K == 0:
                dp[i][j] = cum_sum[M]
            else:
                if 1 <= j-K:
                    dp[i][j] += cum_sum[j-K]
                if j+K <= M:
                    dp[i][j] += cum_sum[M] - cum_sum[j+K-1]
            dp[i][j] %= MOD
    ans = sum(dp[N]) % MOD
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, M, K)


if __name__ == '__main__':
    main()
