#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, D: int, E: int, F: int, X: int):
    aoki = 0
    takahashi = 0
    time = X
    while time > 0:
        if time < A:
            aoki += time * B
            break
        else:
            aoki += A * B
            time -= A
        time -= C
    time = X
    while time > 0:
        if time < D:
            takahashi += time * E
            break
        else:
            takahashi += D * E
            time -= D
        time -= F
    if takahashi < aoki:
        print("Takahashi")
    elif aoki < takahashi:
        print("Aoki")
    else:
        print("Draw")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F, X)


if __name__ == '__main__':
    main()
