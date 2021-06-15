#!/usr/bin/env python3
import sys
import math

def solve(T: int, L: int, X: int, Y: int, Q: int, E: "List[int]"):
    for i in range(Q):
        y2 = -L/2*math.sin(math.pi*360*E[i]/T/180)
        z2 = L/2-L/2*math.cos(math.pi*360*E[i]/T/180)
        s = (X**2 + abs(y2-Y)**2)**0.5
        print(math.degrees(math.atan2(z2, s)))   
        
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    E = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(T, L, X, Y, Q, E)

if __name__ == '__main__':
    main()
