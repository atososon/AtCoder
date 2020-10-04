n,s = map(str, input().split())
ans = 0
dic={(0,0):1}
c1 = 0
c2 = 0
for i in range(int(n)):
    if s[i]=="A":
        c1+=1
    elif s[i]=="T":
        c1-=1
    elif s[i]=="G":
        c2+=1
    else:
        c2-=1
    ans+=dic.get((c1,c2),0)
    dic[(c1,c2)]=dic.get((c1,c2),0)+1
print(ans)