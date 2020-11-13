x = int(input())
f = x % 100
s = x // 100
ans = f - 5 * s
if ans <= 0:
    print("1")
else:
    print("0")