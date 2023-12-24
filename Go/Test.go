package main;

import (
 "fmt"
 "time"
);

func main() {

  massive := [2][2]int{{1, 2}, {3, 4}}
  
  fmt.Println(massive)
  
	c1 := make(chan string)
  c2 := make(chan string)

  go func() { //горутины топ ез бот
      time.Sleep(0 * time.Second)
      c1 <- "s"
  }()
  go func() {
    time.Sleep(5 * time.Second)
    c2 <- "two"
	}()

  for {
    select { //конченая вещь
      case msg1 := <-c1:
        fmt.Println("received", msg1)
      case msg2 := <-c2:
        fmt.Println("received", msg2)
      default :
        break
    }
  }
  
}