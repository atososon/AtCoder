package main

import "fmt"

func min(a1 int64, a2 int64, a3 int64, a4 int64) int64 {
	switch {
	case a1 <= a2 && a1 <= a3 && a1 <= a4:
		return a1
	case a2 <= a1 && a2 <= a3 && a2 <= a4:
		return a2
	case a3 <= a1 && a3 <= a2 && a3 <= a4:
		return a3
	default:
		return a4
	}
}
func main() {
	// Failed to predict input format
	var a1, a2, a3, a4 int64
	fmt.Scan(&a1, &a2, &a3, &a4)
	fmt.Println(min(a1, a2, a3, a4))
}
