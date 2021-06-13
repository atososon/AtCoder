#!/usr/bin/env python3
import sys


def solve(H: int, W: int, A: "List[List[int]]"):
    w = [0]*W
    h = [0]*H
    
    for i in range(H):
        for j in range(W):
            h[i] += A[i][j]
    
    for i in range(W):
        for j in range(H):
            w[i] += A[j][i]
    
    for i in range(H):
        for j in range(W):
            A[i][j] = h[i] + w[j] - A[i][j]
        
    for i in range(H):
        print(*A[i])
            
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A)

if __name__ == '__main__':
    main()