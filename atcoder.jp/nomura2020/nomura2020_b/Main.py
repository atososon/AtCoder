t = list(input())
for i in range(len(t)):
    if t[i]=="?":
        if i==0 and len(t)!=1:
            if t[i+1]=="D" or t[i+1]=="?":
                t[i] = "P"
                t[i+1] = "D"
            else:
                t[i] = "D"
        elif i!=len(t)-1:
            if t[i-1]=="P":
                t[i] = "D"
            elif t[i+1]=="D" or t[i+1]=="?":
                t[i] = "P"
                t[i+1] = "D"
            else:
                t[i] = "D"
        else:
            t[i] = "D"
print(*t,sep="")