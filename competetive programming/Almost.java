import java.util.ArrayList;
import java.util.List;

import java.util.Arrays;

class Almost{
	static public void main(String[] args){
		
		int[] a = {9,9,9,9};
		// 
		//"498828660196"
		//"840477629533"
		String num1 = "9999";
		String num2 = "9999";
		
		char[] x = num1.toCharArray();
		char[] y = num2.toCharArray();
		String add = "";
		//String h = Character.toString(x[i]);
		//int k = Integer.parseInt(h);
		int num = 0;
		int carry =0 ;
		if(x.length>=y.length){
			for(int i=1;i<=x.length;i++){
				
				int g = (x[x.length-i] - '0')+(y[y.length-i]-'0');
				g = (x[x.length-i] - '0')+(y[y.length-i]-'0')+carry;	
				if(g>=10){
					num = g-10;
					carry = 1;
				}

				System.out.println(g);		
					

			}
		}		



	}
}