n = int(input())
a = list(map(int, input().split()))
s = sum(a)
s2 = sum(map(lambda x:x*x, a))
print((s**2-s2)//2 % (10**9+7))