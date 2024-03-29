#!/usr/bin/env python3
import sys


def solve(x: "List[int]", y: "List[int]"):
    ans = list()
    if x[0] == x[1]:
        ans.append(x[2])
    elif x[0] == x[2]:
        ans.append(x[1])
    else:
        ans.append(x[0])
    if y[0] == y[1]:
        ans.append(y[2])
    elif y[0] == y[2]:
        ans.append(y[1])
    else:
        ans.append(y[0])
    print(*ans)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = [int()] * (3)  # type: "List[int]"
    y = [int()] * (3)  # type: "List[int]"
    for i in range(3):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(x, y)


if __name__ == '__main__':
    main()
