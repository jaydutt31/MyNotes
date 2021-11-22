class Helpp{
	public static void main(String[] args) throws StringIndexOutOfBoundsException
	{ 

		String[] strs = {"flower","flow","flight"};
		String[] s = {"dog","racecar","car"};

		StringBuilder x = new StringBuilder();
		
		System.out.println(strs.length);
		
		for(int i = 0; i<strs.length-1;i++)
			{
		//System.out.println(strs[i]+strs[i+1]);
			if(strs.length<=1){ break; }
			else{
				String y = strs[i];
				String z = strs[i+1];
				if(y.length()<z.length()){
					
					for(int j=0;j<=y.length();j++){

						if(y.charAt(j)==z.charAt(j)){
							x.append(z.charAt(j));
						}else{break;}

					}}
				else{for(int j=0;j<=z.length();j++){
					if(y.charAt(j)==z.charAt(j)){
							x.append(z.charAt(j));
					}else{break;}
				}
			}
		}
	}
}
}


					
		
				
			


			



	