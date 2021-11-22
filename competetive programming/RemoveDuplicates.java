import java.util.HashSet;

class Solution{
    public static void main(String[] args){
        

        // HashSet
            
        int[] inputArray = {1,2,3,4,5,6,7,7,7,7};
        HashSet<Integer> set = new HashSet<Integer>();
        for (int element : inputArray) 
        {
        if( ! set.add(element))
        {
        System.out.println("Duplicate Element : "+element);
        }
        }
        }
        
      
       
    }
  