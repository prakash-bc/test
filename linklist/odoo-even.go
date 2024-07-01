package main

import (
	"fmt"
	"sync"
	"time"
)

// Print odd and even in separate go routines
func main() {
	printOdd := make(chan bool)

	var wg = new(sync.WaitGroup)
	wg.Add(1)
	go OddPrinter(printOdd, wg)
	wg.Add(1)
	go EvenPrinter(printOdd, wg)
	printOdd <- true
	wg.Wait()

}

func OddPrinter(printOdd chan bool, wg *sync.WaitGroup) {
	defer wg.Done()
	var i = 1
	for true {
		<-printOdd
		fmt.Println("odd number:", i)
		time.Sleep(1 * time.Second)
		printOdd <- true
		i += 2

	}
}

func EvenPrinter(printOdd chan bool, wg *sync.WaitGroup) {
	defer wg.Done()
	var i = 0
	for true {
		<-printOdd
		fmt.Println("even number:", i)
		time.Sleep(1 * time.Second)
		printOdd <- true
		i += 2
	}
}
