package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const YES = "Yes"
const NO = "No"

func solve(S string) {
	ans := YES
	for i := 0; i < len(S); i++ {
		u := strings.ToUpper(S[i : i+1])
		if i%2 == 0 && u == S[i:i+1] {
			ans = NO
		} else if i%2 == 1 && u != S[i:i+1] {
			ans = NO
		}
	}
	fmt.Println(ans)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const initialBufSize = 4096
	const maxBufSize = 1000000
	scanner.Buffer(make([]byte, initialBufSize), maxBufSize)
	scanner.Split(bufio.ScanWords)
	var S string
	scanner.Scan()
	S = scanner.Text()
	solve(S)
}
