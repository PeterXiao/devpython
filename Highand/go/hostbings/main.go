// hostbings project main.go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	req, err := http.NewRequest("GET", "http://docs.python.org/3.4/whatsnew/3.4.html", nil)
	if err != nil {
		panic(err)
	}
	req.Host = "www.studygolang.com"
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(body))
}
