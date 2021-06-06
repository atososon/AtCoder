import sys
sys.setrecursionlimit(10000)

def dfs(v):
    if temp[v]: 
        return 
    temp[v] = True
    for vv in g[v]:
        dfs(vv)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
ans = 0
for i in range(n):
    temp = [False] * n
    dfs(i)
    ans += sum(temp)

print(ans)