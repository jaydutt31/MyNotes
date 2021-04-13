package main

import "fmt"

func main(){
	a := 4
	SquareVal(a)

}

func SquareVal(v int){
	v *= v
	fmt.Println(&v, v)
}

func squareAdd(p *int){
	*p *= *p
	fmt.Println(p, *p )
}
