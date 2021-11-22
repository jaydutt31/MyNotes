import java.util.HashMap;
import java.lang.*;

class Test {
    public static void main(String[] args){

        String s = "IMXXXX"; 


        HashMap<Character, Integer> map = new HashMap<>();

        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        int num = 0;

        for(int i = 0;i<=s.length()-1;i++){
         
            if(i<(s.length()-1) && map.get(s.charAt(i)) < map.get(s.charAt(i+1))){

                num -= map.get(s.charAt(i));

            }else{
                num+=map.get(s.charAt(i));
            }


        }
        System.out.println(num);
        
    }
}