#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", C: "List[int]"):
    b_poly = list()
    c = C[::-1]
    a = A[::-1]
    for i in range(M+1):
        s = c[i] // a[0]
        for j in range(i, i+N+1):
            c[j] -= a[j-i] * s
        b_poly.append(s)
    print(*b_poly[::-1])

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N + M + 1)]  # type: "List[int]"
    solve(N, M, A, C)


if __name__ == '__main__':
    main()
