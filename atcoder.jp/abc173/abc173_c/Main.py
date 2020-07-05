h,w,k = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for ib in range(1<<h):
    for jb in range(1<<w):
        cc = 0
        for i in range(h):
            if ib&(1<<i):
                continue
            for j in range(w):
                if jb&(1<<j):
                    continue
                cc += c[i][j]=="#"
        if cc==k:
            ans += 1
print(ans) 