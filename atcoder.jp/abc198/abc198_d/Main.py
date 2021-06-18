#!/usr/bin/env python3
import sys
import itertools

def solve(S: "List[str]"):
    li = list()
    for i in S:
        for j in range(len(i)):
            li.append(i[j])
    s = list(set(li))
    if len(s) >= 11:
        print("UNSOLVABLE")
        return
    else:
        p = itertools.permutations([0,1,2,3,4,5,6,7,8,9], len(s))
        for v in p:
            s1 = ""
            s2 = ""
            s3 = ""
            for ss in S[0]:
                s1 += str(v[s.index(ss)])
            for ss in S[1]:
                s2 += str(v[s.index(ss)])
            for ss in S[2]:
                s3 += str(v[s.index(ss)])
            if s1[0] == "0" or s2[0] == "0" or s3[0] == "0":
                continue
            if int(s1)+int(s2) == int(s3):
                print(s1)
                print(s2)
                print(s3)
                return
    print("UNSOLVABLE")
    return


# Generated by 2.4.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(S)

if __name__ == '__main__':
    main()