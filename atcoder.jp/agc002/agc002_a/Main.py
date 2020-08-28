a,b = map(int, input().split())
if a<=0<=b:
    print("Zero")
elif a>0 and b>0 or b<0 and (a-b)%2==1:
    print("Positive")
else:
    print("Negative")