package LinkedList;
/*

LinkedList: Collection of element where every element is linked to each other. 

we use a concept of data and reference.

Head = first element[i.e node]

LinkedList =  12,6,8,3
              <-Nodes->

Head -> [12][326] --> [6][102] --> [8][202] --> [3][NULL]
        [512]         [326]        [102]        [202] 

To add:

Head -> [12][326] --> [6][102] --> [8][202] --> [3][126]
        [512]         [326]        [102]        [202] 
                                                  🠗
                                                  🠗
                                                [7][NULL]

1. Create a node, add value.
2. replace "Null" with new node's address.
3. add "Null" as the next node's address.

uses O(n)
                                
*/ 



public class LinkedlistImp {

    Node head;
    public void insert(int data){
        Node node = new Node();
        node.data = data;
    }
    
}
