package main

import "fmt"

func main(){
	i, j := 43, 2701
	fmt.Println(&i, &j);

	p := &i
	fmt.Println(*p)  // dereferencing  

}




// pointers are used excess variable from here and there 
// than copying an modifying it everytime, which is inefficient

// whenever we try to run a code, a goroutine is formed and it creates a stack
// goroutine is an independent path of executuion, as a thread
// for every function call, goroutine creates a frame inside a stack
// every frame is isolated, 
// eg, pointers.go