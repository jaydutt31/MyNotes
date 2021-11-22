public class ArrayImp{
    public static void main(String[] args){

        int x[] = {5,8,7,2};
        System.out.println(x);

    }
}
/*

one [byte] address only stores a single piece of information, 
eg, int x=5
[addr=102] = 5

in Java, 4 bytes.  [in c, 2 bytes]

int x[] = 5,8,7,2;

[101][105][109][113] = 5,8,7,2 #contiguous
 <-----address----->  <-values->

fetch elements, 
x[index_number] = values at index
x[0] = 5
x[1] = 8

uses O(1)
  
Arrays in java is immutable, size cannot be changed. 

Dynamic array : To expand, Create a seperate array of 2n element.



*/

