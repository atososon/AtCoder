package main

import "fmt"

func main() {
	var c string
	fmt.Scan(&c)
	if c[0:1] == c[1:2] && c[1:2] == c[2:3] {
		fmt.Println("Won")
	} else {
		fmt.Println("Lost")
	}
}
