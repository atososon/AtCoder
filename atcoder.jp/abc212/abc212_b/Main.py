#!/usr/bin/env python3


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    x = input()
    if x[0] == x[1] == x[2] == x[3] or str(int(x[0]) + 1)[-1] == str(int(x[1]))[-1] and str(int(x[1])+1)[-1] == str(int(x[2]))[-1] and str(int(x[2])+1)[-1] == str(int(x[3]))[-1]:
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()
