import statistics
a, b, c = map(int, input().split())
if a%2 == b%2 == c%2 == 1:
    ans = min(a, b, c) * statistics.median([a, b, c])
else:
    ans = 0
print(ans)