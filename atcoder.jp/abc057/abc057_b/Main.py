n, m = map(int, input().split())
ab = list()
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a,b])
cd = list()
for i in range(m):
    c, d = map(int, input().split())
    cd.append([c,d])
for i in range(n):
    ans = {}
    for j in range(m):
        ans[j+1] = abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1])
    print(sorted(ans.items(), key=lambda x:x[1])[0][0])