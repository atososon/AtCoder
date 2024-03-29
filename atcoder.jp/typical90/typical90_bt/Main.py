#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)


def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def dfs(i, j, distance=0):
        visitted[i][j] = True
        for r, l in direction:
            rn = i + r
            cn = j + l
            if 0 <= rn < h and 0 <= cn < w and c[rn][cn] == ".":
                if visitted[rn][cn]:
                    dist[rn][cn] = max(dist[rn][cn], distance + 1)
                else:
                    dfs(rn, cn,  distance+1)
    ans = 0
    for i in range(h):
        for j in range(w):
            visitted = [[False for _ in range(w)] for _ in range(h)]
            dist = [[-1 for _ in range(w)] for _ in range(h)]
            dfs(i, j)
            ans = max(ans, dist[i][j])
    if ans <= 2:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
