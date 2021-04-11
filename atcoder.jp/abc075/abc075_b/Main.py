h, w = map(int, input().split())
s = list(input() for _ in range(h))
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            if h == 1 and w == 1:
                s[i] = str(0)
            
            elif h == 1 and j == 0:
                l = [s[0][1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            elif h == 1 and j == w-1:
                l = [s[0][w-2]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
            
            elif h == 1:
                l = [s[i][j-1], s[i][j+1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            elif w == 1 and i == 0:
                l = [s[1][0]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                    
            elif w == 1 and i == h-1:
                l = [s[h-2][0]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                    
            elif w == 1:
                l = [s[i-1][j], s[i+1][j]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                    
            elif i == 0 and j == 0:
                l = [s[i+1][j], s[i][j+1], s[i+1][j+1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            elif i == h-1 and j == 0:
                l = [s[i-1][j], s[i][j+1], s[i-1][j+1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            elif i == 0 and j == w-1:
                l = [s[i][j-1], s[i+1][j], s[i+1][j-1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            elif i == h-1 and j == w-1:
                l = [s[i-1][j], s[i][j-1], s[i-1][j-1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            elif i == 0:
                l = [s[i][j-1], s[i][j+1], s[i+1][j-1], s[i+1][j], s[i+1][j+1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
            
            elif i == h-1:
                l = [s[i][j-1], s[i][j+1], s[i-1][j-1], s[i-1][j], s[i-1][j+1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
            
            elif j == 0:
                l = [s[i-1][j], s[i+1][j], s[i-1][j+1], s[i][j+1], s[i+1][j+1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            elif j == w-1:
                l = [s[i-1][j], s[i+1][j], s[i-1][j-1], s[i][j-1], s[i+1][j-1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]
                
            else:
                l = [s[i-1][j-1], s[i-1][j], s[i-1][j+1], s[i][j-1], s[i][j+1], s[i+1][j-1], s[i+1][j], s[i+1][j+1]]
                s[i]= s[i][:j] + str(l.count("#")) + s[i][j+1:]

for st in s:
    print(*st, sep="")