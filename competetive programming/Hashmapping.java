import java.util.HashMap;

class Hashmapping{
	public static void main(String[] args){

		HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
		
		int[] nums= {1,2,3,4,5,6,7,8,9};

		int target= 17;
		int comp = 0;

		//Solution using hashmap
		for(int x=0;x<nums.length;x++){

			comp = target - nums[x];
			if(map.containsKey(comp)){
				System.out.println(nums[x]+" "+comp);
			}
			else{
			map.put(nums[x],x);
			}
		}
		System.out.println(map);

	}
}