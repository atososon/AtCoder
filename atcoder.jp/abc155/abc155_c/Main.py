import collections
n=int(input())
s=[input() for i in range(n)]
dic=collections.Counter(s)
ans=[]
largest=max(dic.values())
for keys in dic.keys():
    if dic[keys]==largest:
        ans.append(keys)
ans=sorted(ans)
print(*ans)