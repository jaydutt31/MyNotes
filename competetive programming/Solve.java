

class Solve{
	static public void main(String[] args){

		String[] s1= {"Hello","Hepp","Heppl"};
		String[] s2= {"jaya", "jay", "james"};
		String strs = "";
		

		for(int i=0;i<s1.length-1;i++){
			strs = "";
			if(s1[i].length()>s1[i+1].length()){
				String a = s1[i];
				String b = s1[i+1];

				for(int x=0;x<b.length()-1;x++){
					if(a.charAt(x)==b.charAt(x)){
						if(strs==""){
						strs+=a.charAt(x);
						}
						else{
							String temp = strs;
							strs += a.charAt(x);
							// strs = hel
							// new_strs = he
						}
					} 
				}
				
			}
			else if(s1[i].length()<s1[i+1].length()){
				String a = s1[i];
				String b = s1[i+1];

				for(int y=0;y<a.length()-1;y++){
					if(a.charAt(y)==b.charAt(y)){
						strs+=a.charAt(y);
					}
				}
			
			}

			

		}
		System.out.println(strs);

	}
}