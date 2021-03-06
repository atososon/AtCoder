#!/usr/bin/env python3
import sys


def solve(N: int, L: int, K: int, A: "List[int]"):
    left = 0
    right = L // K + 1
    while True:
        M = (left + right) // 2
        f = False
        count = 0
        s = A[0]
        for i in range(N):
            if s >= M:
                count += 1
                s = 0
            if i < N-1:
                s += A[i+1] - A[i]
            if count == K:
                if L-A[i] >= M:
                    f = True
                    break
                else:
                    break
        if f:
            left = M
        else:
            right = M
        if right - left <= 1:
            print(left)
            break
            
    return


# Generated by 2.4.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L, K, A)

if __name__ == '__main__':
    main()
