n,a,b = map(int, input().split())
s = input()
count = 0
count_b = 0
for i in range(len(s)):
    if s[i]=="a":
        if(count < a+b):
            print("Yes")
            count += 1
        else:
            print("No")
    elif s[i]=="b":
        count_b += 1
        if count < a+b and count_b <= b:
            print("Yes")
            count += 1
        else:
            print("No")
    else:
        print("No")