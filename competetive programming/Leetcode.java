import java.util.ArrayList;
import java.util.HashMap;

class Leetcode{
	static public void main(String[] args){

		int[] nums= {1,2,4,6,7,8};
		int target = 5;



		//-------------------------- Brute Force Method  --------------------------
		/*
		int ans[] = new int[2];
		
		for(int i=0;i<nums.length;i++){
			int x = nums[i];
			for(int j=i+1;j<=nums.length-1;j++){
				int y = nums[j];
				if((x+y)==target){
					System.out.println(i+" "+j);
					ans[0]=i+1;
					ans[1]=j+1;
					
				}
			}
		}
		*/
		

		
		

		// --------------------------  Solution using hashmap  --------------------------
		/*
		int comp=0;
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

		for(int x=0;x<nums.length;x++){

			comp = target - nums[x];
			if(map.containsKey(comp)){

				System.out.println((map.get(comp)+1)+" "+(x+1));
			}
			else{
			map.put(nums[x],x);
			}
		}
		*/

		// --------------------------  using two pointers  --------------------------
		
		int start = 0;
		int end = nums.length-1;
		
		while(start<end){
			int i = (nums[start] + nums[end]);
			if(i<target){
				start++;
			}
			else if(i>target){
				end--;
			}
			else{
				System.out.println((start+1)+" "+(end+1));
				break;
			}
		}
			
		
	}
}