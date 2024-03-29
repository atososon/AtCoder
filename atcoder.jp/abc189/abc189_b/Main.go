package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func solve(N int64, X int64, V []int64, P []int64) {
	X *= 100
	var ans int64
	ans = 0
	for i := int64(0); i < N; i++ {
		ans += V[i] * P[i]
		if ans > X {
			fmt.Println(i + 1)
			return
		}
	}
	fmt.Println(-1)
	return
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
	var X int64
	scanner.Scan()
	X, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	V := make([]int64, N)
	P := make([]int64, N)
	for i := int64(0); i < N; i++ {
		scanner.Scan()
		V[i], _ = strconv.ParseInt(scanner.Text(), 10, 64)
		scanner.Scan()
		P[i], _ = strconv.ParseInt(scanner.Text(), 10, 64)
	}
	solve(N, X, V, P)
}
