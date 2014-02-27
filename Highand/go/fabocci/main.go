// fabocci project main.go
package main

import "fmt"

// fibonacci 函数会返回一个返回 int 的函数。
func fibonacci() func() int {

	a := 0
	b := 1
	n := 0
	return func() int {
		if n == 0 {
			n++
			return a
		} else if n == 1 {
			n++
			return b
		}
		a, b = b, a+b
		return b
	}

}
func fibonacci2(num int) int {
	if num < 2 {
		return 1
	}
	return fibonacci2(num-1) + fibonacci2(num-2)
}

// fib returns a function that returns
// successive Fibonacci numbers.
func fib() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
