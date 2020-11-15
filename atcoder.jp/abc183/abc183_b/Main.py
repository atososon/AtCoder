sx, sy, gx, gy = map(int, input().split())
ans = (sy*gx + sx*gy) / (sy + gy)
print(ans)