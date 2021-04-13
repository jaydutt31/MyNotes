package main

import "fmt"
// AlphabetSize is the number of possible characters in the tree
const AlphabetSize = 26

//node represents each node in trie
type Node struct{
	children [26]*Node
	isEnd bool
}

//Trie represent a trie and has a pointer
type Trie struct{
	root *Node 
}

// InitTrie will create a new trie
func InitTrie() *Trie{
	result := &Trie{root:&Node{}}
	return result
}

//insert will take a word and insert it to the trie
func (t *Trie) Insert(w string){
	wordLength := len(w)
	currentNode := t.root
	for i:=0;i<wordLength;i++{
		charIndex := w[i] - 'a'
		if currentNode.children[charIndex] == nil{
			currentNode.children[charIndex] = &Node{}
		} 
		currentNode=currentNode.children[charIndex]
	}
	currentNode.isEnd = true
}

//search will take a word and Return true if that word is included in the trie
func (t *Trie) Search(w string) bool {
	wordLength := len(w)
	currentNode := t.root
	for i:=0;i<wordLength;i++{
		charIndex := w[i] - 'a'
		if currentNode.children[charIndex] == nil{
			return false
		} 
		currentNode=currentNode.children[charIndex]
	}
	if currentNode.isEnd == true{
		return true
	}

	return false
}

func main(){
	myTrie := InitTrie()
	myTrie.Insert("anagram")
	myTrie.Search("anagram")
	toAdd := []string{
		"aragorn",
		"argon",
		"aragon",
		"eragon",
		"oregon",
		"oregano",
		"oreo",
	}

	for _,v := range toAdd{
		myTrie.Insert(v)
	}
	fmt.Println(myTrie.Search("argonwin"))
}