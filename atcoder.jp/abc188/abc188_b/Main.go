package main

import (
	"bufio"
	"os"
	"strconv"
    "fmt"
)

const YES = "Yes"
const NO = "No"

func solve(N int64, A []int64, B []int64) {
    var ans int64
    ans = 0
    for i := int64(0); i < N; i++ {
        ans += A[i]*B[i]
    }
    if ans == 0{
        fmt.Println(YES)
    } else{
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
    A := make([]int64, N)
    for i := int64(0); i < N; i++ {
        scanner.Scan()
        A[i], _ = strconv.ParseInt(scanner.Text(), 10, 64)
    }
    B := make([]int64, N)
    for i := int64(0); i < N; i++ {
        scanner.Scan()
        B[i], _ = strconv.ParseInt(scanner.Text(), 10, 64)
    }
	solve(N, A, B)
}
