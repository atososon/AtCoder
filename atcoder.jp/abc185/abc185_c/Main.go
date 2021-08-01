package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func solve(L int64) {
	var ans int64
	ans = 1
	for i := int64(L - 11); i <= int64(L-1); i++ {
		ans = ans * i / int64(math.Abs(float64(12+(i-L))))
	}
	fmt.Println(ans)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const initialBufSize = 4096
	const maxBufSize = 1000000
	scanner.Buffer(make([]byte, initialBufSize), maxBufSize)
	scanner.Split(bufio.ScanWords)
	var L int64
	scanner.Scan()
	L, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	solve(L)
}
