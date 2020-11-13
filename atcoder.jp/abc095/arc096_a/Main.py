a, b, c, x, y = map(int, input().split())
if a+b > 2*c:
    if max(x,y) * 2 * c <= c * x * 2 + (y-x) * b or max(x,y) * 2 * c <= c * y * 2 + (x-y) * a:
        ans = max(x,y) * 2* c
    elif x <= y:
        ans = c * x * 2 + (y-x) * b
    else:
        ans = c * y * 2 + (x-y) * a

else:
    ans = a * x + b * y
print(ans)