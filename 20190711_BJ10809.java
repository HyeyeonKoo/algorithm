import java.util.Scanner;

public class Main {
	
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		int[] num = new int[26];
		for(int i=0; i<num.length; i++) {
			num[i] = -1;
		}
		
		for(int i=0; i<str.length(); i++) {
			char ch = str.charAt(i);
			if(num[(int)ch - 97]<i && num[(int)ch - 97] != -1) {
				continue;
			}else {
				num[(int)ch - 97] = i;				
			}
		}
		
		for(int i=0; i<num.length; i++) {
			System.out.print(num[i] + " ");
		}
		
	}

}
