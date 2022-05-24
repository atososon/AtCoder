#!/usr/bin/env python3
import sys
import bisect


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def solve(K: int):
    divisors = make_divisors(K)
    ans = 0
    for a in divisors:
        if a ** 3 > K:
            break
        bc = K // a
        for b in divisors:
            if b < a or bc % b != 0:
                continue
            c = bc // b
            if b > c:
                break
            ans += 1

    print(ans)
    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == '__main__':
    main()