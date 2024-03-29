package main

import (
	"bufio"
	"os"
	"strconv"
	"fmt"
	"math"
)

const YES = "Yes"
const NO = "No"

func solve(X int64, Y int64) {
	if math.Abs(float64(X-Y)) < 3 {
		fmt.Println(YES)
	}else {
		fmt.Println(NO)
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const initialBufSize = 4096
	const maxBufSize = 1000000
	scanner.Buffer(make([]byte, initialBufSize), maxBufSize)
	scanner.Split(bufio.ScanWords)
	var X int64
    scanner.Scan()
    X, _ = strconv.ParseInt(scanner.Text(), 10, 64)
    var Y int64
    scanner.Scan()
    Y, _ = strconv.ParseInt(scanner.Text(), 10, 64)
	solve(X, Y)
}
