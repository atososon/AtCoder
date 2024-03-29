#!/usr/bin/env python3
from cmath import e
import sys


def solve(N: int, K: int, A: "List[int]", X: "List[int]", Y: "List[int]"):
    ans = 0
    for i in range(N):
        euclidean_distances = list()
        for a in A:
            a -= 1
            euclidean_distance = (X[i] - X[a]) ** 2 + (Y[i] - Y[a]) ** 2
            euclidean_distances.append(euclidean_distance)
        ans = max(ans, min(euclidean_distances))
    print(ans ** 0.5)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, K, A, X, Y)


if __name__ == '__main__':
    main()
