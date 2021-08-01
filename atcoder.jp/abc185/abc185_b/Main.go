package main

import "fmt"

const YES = "Yes"
const NO = "No"

func main() {
	var n, m, t, v, time int64
	fmt.Scan(&n, &m, &t)
	v = n
	time = 0
	ans := YES
	for i := int64(0); i < m; i++ {
		var a, b int64
		fmt.Scan(&a, &b)
		v -= a - time
		if v <= 0 {
			ans = NO
		}
		v += b - a
		if v > n {
			v = n
		}
		time = b
	}
	if v-(t-time) <= 0 {
		ans = NO
	}
	fmt.Println(ans)
}
