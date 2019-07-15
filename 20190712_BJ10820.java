import java.util.Scanner;

public class Main {
	
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNextLine()) {
			
			String str = sc.nextLine();
			int lower = 0;
			int upper = 0;
			int number = 0;
			int gap = 0;
			
			for(int i=0; i<str.length(); i++) {
				
				char ch = str.charAt(i);
				
				if(ch>='a' && ch <= 'z') {
					lower++;
				}else if(ch>='A' && ch<='Z') {
					upper++;
				}else if(ch>='0' && ch<='9') {
					number++;
				}else if(ch == ' ') {
					gap++;
				}
			}
			
			System.out.println(lower + " " + upper + " " + number + " " + gap);
			
		}
		
	}

}
