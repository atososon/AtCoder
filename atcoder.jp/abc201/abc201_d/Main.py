#!/usr/bin/env python3


# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            f = (i+j)%2
            if i==h-1 and j==w-1:
                continue
            elif i == h-1:
                if f == 0:
                    if a[i][j+1] == "+":
                        dp[i][j] = dp[i][j+1] + 1
                    else:
                        dp[i][j] = dp[i][j+1] - 1
                        
                else:
                    if a[i][j+1] == "+":
                        dp[i][j] = dp[i][j+1] - 1
                    else:
                        dp[i][j] = dp[i][j+1] + 1
            elif j == w-1:
                if f == 0:
                    if a[i+1][j] == "+":
                        dp[i][j] = dp[i+1][j] + 1
                    else:
                        dp[i][j] = dp[i+1][j] - 1
                        
                else:
                    if a[i+1][j] == "+":
                        dp[i][j] = dp[i+1][j] - 1
                    else:
                        dp[i][j] = dp[i+1][j] + 1
            else:
                if f == 0:
                    if a[i+1][j] == "+":
                        t1 = 1
                    else:
                        t1 = -1
                    if a[i][j+1] == "+":
                        t2 = 1
                    else:
                        t2 = -1
                    dp[i][j] = max(dp[i+1][j]+t1, dp[i][j+1]+t2)
                else:
                    if a[i+1][j] == "+":
                        t1 = -1
                    else:
                        t1 = 1
                    if a[i][j+1] == "+":
                        t2 = -1
                    else:
                        t2 = 1
                    dp[i][j] = min(dp[i+1][j]+t1, dp[i][j+1]+t2)
            
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")
if __name__ == '__main__':
    main()