def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
s, p = map(int, input().split())
f = 0
m = make_divisors(p)
for i in range(0, len(m)//2+1):
    if m[i] * m[-1*i-1] == p and m[i] + m[-1*i-1] == s:
        f = 1
        break

if f == 1:
    print("Yes")
else:
    print("No")