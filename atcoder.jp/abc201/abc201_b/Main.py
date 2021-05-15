n = int(input())
mount = dict()
for i in range(n):
    s, t = input().split()
    mount[s] = int(t)
mount_sorted = sorted(mount.items(), key=lambda x:x[1])
print(mount_sorted[-2][0])