package main

import "fmt"


var count int
// Node represents the component of binary tree
type Node struct{
	Key int
	Left *Node
	Right *Node
}


// Insert
func (n *Node) Insert (k int) {
	if n.Key < k {
		//move right
		if n.Right == nil{
			n.Right = &Node{Key: k}
		} else {
			n.Right.Insert(k)
		}
	} else if n.Key > k {
		//move left
		if n.Left == nil{
			n.Left = &Node{Key: k}
		} else {
			n.Left.Insert(k)
		}

	}
}


// Search will take in a key value
// and RETURN true if exists
func (n *Node) Search (k int) bool{

	count ++

	if n == nil{
		return false
	}

	if n.Key < k {
		//move right
		return n.Right.Search(k)
	} else if n.Key > k {
		//move left
		return n.Left.Search(k)
	}
	return true
}



func main(){
	tree := &Node{Key: 100}
	tree.Insert(250)
	tree.Insert(300)
	tree.Insert(50)
	fmt.Println(tree)
	tree.Insert(2)
	tree.Insert(309)
	tree.Insert(59)
	tree.Insert(25)
	tree.Insert(30)
	tree.Insert(56)
	fmt.Println(tree.Search(2))
	fmt.Println(count)

}