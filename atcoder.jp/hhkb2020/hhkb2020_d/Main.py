t = int(input())
def s(z):
    return z*(z+1)//2
for _ in range(t):
    n, a, b = map(int, input().split())
    if a+b > n:
        print(0)
    else:
        print((s(n-a-b+1)*((n-a+1)*(n-b+1)-s(n-a-b+1))*4)%(10**9+7))