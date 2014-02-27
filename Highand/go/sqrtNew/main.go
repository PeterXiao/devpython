// sqrtNew project main.go
package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	//var z = 3.05
	//for
	//z = z - (z*z-x)/(2*z)
	//return z
	z := 1.0
	z_last := 1.0
	z_limit := 0.0000001
	if x > 0 {
		for {
			z = (z + x/z) / 2
			if math.Abs(z_last-z) < z_limit {
				break
			}
			z_last = z
		}
	}
	return z

}

func main() {
	fmt.Println(Sqrt(2))
}
