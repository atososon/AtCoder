a = input()
m = ["-","+"]
for i in m:
    for j in m:
        for k in m:
            if eval(a[0] + i + a[1] + j + a[2] + k + a[3]) == 7:
                print(a[0] + i + a[1] + j + a[2] + k + a[3] + "=7")
                exit()