package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func g1(x int) int {
	var s string
	var ans int
	s = strconv.Itoa(x)
	var s1 []string
	for i := 0; i < len(s); i++ {
		s1 = append(s1, s[i:i+1])
	}
	sort.Sort(sort.Reverse(sort.StringSlice(s1)))
	var s2 string
	for i := 0; i < len(s1); i++ {
		s2 += s1[i]
	}
	ans, _ = strconv.Atoi(s2)
	return ans
}

func g2(x int) int {
	var s string
	var ans int
	s = strconv.Itoa(x)
	var s1 []string
	for i := 0; i < len(s); i++ {
		s1 = append(s1, s[i:i+1])
	}
	sort.Strings(s1)
	var s2 string
	for i := 0; i < len(s1); i++ {
		s2 += s1[i]
	}
	ans, _ = strconv.Atoi(s2)
	return ans
}

func f(x int) int {
	return g1(x) - g2(x)
}

func solve(N int64, K int64) {
	var ans int
	ans = int(N)
	for i := int64(0); i < K; i++ {
		judge := f(ans)
		if ans == judge {
			break
		}
		ans = judge
	}
	fmt.Println(ans)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const initialBufSize = 4096
	const maxBufSize = 1000000
	scanner.Buffer(make([]byte, initialBufSize), maxBufSize)
	scanner.Split(bufio.ScanWords)
	var N int64
	scanner.Scan()
	N, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	var K int64
	scanner.Scan()
	K, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	solve(N, K)
}
