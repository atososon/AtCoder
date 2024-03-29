package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(x int64, y int64) int64 {
	if x < y {
		return y
	} else {
		return x
	}
}
func solve(a int64, b int64, c int64, d int64) {
	fmt.Println(max(max(a-c, b-c), max(a-d, b-d)))
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const initialBufSize = 4096
	const maxBufSize = 1000000
	scanner.Buffer(make([]byte, initialBufSize), maxBufSize)
	scanner.Split(bufio.ScanWords)
	var a int64
	scanner.Scan()
	a, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	var b int64
	scanner.Scan()
	b, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	var c int64
	scanner.Scan()
	c, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	var d int64
	scanner.Scan()
	d, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	solve(a, b, c, d)
}
