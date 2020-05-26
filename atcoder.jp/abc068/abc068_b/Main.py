n = int(input())
while True:
    temp = n
    while temp%2==0:
        temp /= 2
    if temp==1:
        print(n)
        break
    n-=1