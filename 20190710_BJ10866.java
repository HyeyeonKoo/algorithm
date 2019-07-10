import java.util.Scanner;
import java.util.LinkedList;

public class Main {
	
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		
		LinkedList<Integer> list = new LinkedList<Integer>();
		
		for(int i=0; i<n; i++) {
			
			String order = sc.nextLine();
			String orderName = order.split(" ")[0];
			
			if(orderName.equals("push_front")) {
				int orderNum = Integer.parseInt(order.split(" ")[1]);
				//System.out.println(orderNum);
				list.addFirst(orderNum);
			}else if(orderName.equals("push_back")) {
				int orderNum = Integer.parseInt(order.split(" ")[1]);
				//System.out.println(orderNum);
				list.addLast(orderNum);
			}else if(orderName.equals("pop_front")) {
				if(list.isEmpty()) {
					System.out.println("-1");
				}else {
					System.out.println(list.getFirst());
					list.removeFirst();
				}
			}else if(orderName.equals("pop_back")) {
				if(list.isEmpty()) {
					System.out.println("-1");
				}else {
					System.out.println(list.getLast());
					list.removeLast();	
				}
			}else if(orderName.equals("front")) {
				if(list.isEmpty()) {
					System.out.println("-1");
				}else {
					System.out.println(list.getFirst());
				}
			}else if(orderName.equals("back")) {
				if(list.isEmpty()) {
					System.out.println("-1");
				}else {
					System.out.println(list.getLast());
				}
			}else if(orderName.equals("size")) {
				System.out.println(list.size());
			}else if(orderName.equals("empty")) {
				if(list.isEmpty()) {
					System.out.println("1");
				}else {
					System.out.println("0");
				}
			}


		}
		
	}

}
