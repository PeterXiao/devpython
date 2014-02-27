// myhttp project main.go
//package main

//import (
//	"github.com/hoisie/httplib"
//	"io/ioutil"
//)

//func main() {
//	//get the google home page
//	c := new(httplib.Client)
//	resp, err := c.Request("http://www.google.com", "GET", nil, "")
//	data := ioutil.ReadAll(resp.Body)
//	println(string(data))
//}
package main

import (
	"github.com/gorilla/http"
	"log"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatalf("usage: %v $URL", os.Args[0])
	}
	if _, err := http.Get(os.Stdout, os.Args[1]); err != nil {
		log.Fatalf("unable to fetch %q: %v", os.Args[1], err)
	}
}
