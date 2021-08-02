package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func solve(N int64) {
	for i := int64(1); i <= int64(1000000); i++ {
		var s string
		s = strconv.Itoa(int(i)) + strconv.Itoa(int(i))
		var j int
		j, _ = strconv.Atoi(s)
		if int64(j) > N {
			fmt.Println(i - 1)
			return
		}
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
	solve(N)
}
