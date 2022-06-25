#!/usr/bin/env python3
import sys


def solve(N: int):
    A = [[1]*(i+1) for i in range(N)]
    for i in range(N):
        for j in range(1, i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(*A[i])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
