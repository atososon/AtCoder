package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const YES = "Yes"
const NO = "No"

func solve(N int64, D [][]int64) {
	var count int64
	count = 0

	var ans int64
	ans = 0

	for i := int64(0); i < N; i++ {
		if D[i][0] == D[i][1] {
			count += 1
		} else {
			ans = int64(math.Max(float64(ans), float64(count)))
			count = 0
		}
	}
	ans = int64(math.Max(float64(ans), float64(count)))
	if ans >= 3 {
		fmt.Println(YES)
	} else {
		fmt.Println(NO)
	}
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
	D := make([][]int64, N)
	for i := int64(0); i < N; i++ {
		D[i] = make([]int64, 2)
	}
	for i := int64(0); i < N; i++ {
		for j := int64(0); j < 2; j++ {
			scanner.Scan()
			D[i][j], _ = strconv.ParseInt(scanner.Text(), 10, 64)
		}
	}
	solve(N, D)
}
