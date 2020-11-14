a, b, c = map(int, input().split())
m = max(a, b, c) * 3
abc = a + b + c
if abc % 2 == m % 2:
    ans = (m-abc) // 2
else:
    ans = (m-abc) // 2 + 2
print(ans)