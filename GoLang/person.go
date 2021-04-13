package main

import "fmt"


type person struct {
	name string
	age int
}

func initPerson() person /*or "*person" */{
	m := person{name:"noname", age: 50}
	return m       // sends a copy of main in main frame
	return &m      // sends a copy of address of m to main frame 
}

func main() {

	fmt.Println(initPerson())
}



// stack doesnt need grabage collector as if discards the frames
// on completion, but using heaps costs us performance and puts
// burdens on garbage collector.