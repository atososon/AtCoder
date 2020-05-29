x = int(input())
f = 0
while True:
    for i in range(x-1,0,-1):
        if i==1:
            f=1
            print(x)
            break
        if x%i==0:
            break
        
    if f==1:
        break
    x+=1