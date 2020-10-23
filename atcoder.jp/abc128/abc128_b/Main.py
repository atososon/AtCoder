n = int(input())
guidebook = []
for i in range(n):
  item = input().split()
  guidebook.append([item[0], -int(item[1]), i+1])
guidebook.sort()
for i in range(n):
  print(guidebook[i][-1])