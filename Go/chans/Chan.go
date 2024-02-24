package main

import (
	"fmt"
	"time"
)

type ChanStr chan string

func goChan(c1 ChanStr) {
	time.Sleep(time.Second*1)
	fmt.Println("This is", <-c1)
}

func main() {
	c1 := make(ChanStr)
	fmt.Println("Start",)
	go goChan(c1)
	
	cb := make(chan int, 3)
	for i:=1; i<=cap(cb); i++ {
		cb<-i*i
		fmt.Println(<-cb)
	}
	close(cb)
	c1 <- "end"
}