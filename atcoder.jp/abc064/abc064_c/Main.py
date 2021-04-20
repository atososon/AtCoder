m = int(input())
a = list(map(int, input().split()))
check = [0] * 8
free = 0
for i in a:
    if 1<=i<=399:
        check[0] = 1
    elif 400<=i<=799:
        check[1] = 1
    elif 800<=i<=1199:
        check[2] = 1
    elif 1200<=i<=1599:
        check[3] = 1
    elif 1600<=i<=1999:
        check[4] = 1
    elif 2000<=i<=2399:
        check[5] = 1
    elif 2400<=i<=2799:
        check[6] = 1
    elif 2800<=i<=3199:
        check[7] = 1
    elif i>=3200:
        free += 1
ans1 = check.count(1)
ans2 = ans1 + free
print(max(ans1,1), ans2)