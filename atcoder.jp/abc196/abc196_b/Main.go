package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func solve(X string) {
	fmt.Println(strings.Split(X, ".")[0])
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const initialBufSize = 4096
	const maxBufSize = 1000000
	scanner.Buffer(make([]byte, initialBufSize), maxBufSize)
	scanner.Split(bufio.ScanWords)
	var X string
	fmt.Scan(&X)
	solve(X)
}
