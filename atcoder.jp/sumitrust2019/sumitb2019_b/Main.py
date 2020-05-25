n = int(input())
ans = n
while int(ans*1.08) > n:
    ans -= 1
if int(ans*1.08)==n:
    print(ans)
else:
    print(":(")