h,w = map(int, input().split())
s = [input() for i in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if j < w-1:
            if s[i][j]=="." and s[i][j+1]==".":
                ans += 1
        if i < h-1:
            if s[i][j]=="." and s[i+1][j]==".":
                ans += 1
print(ans)