import java.util.*;


public class HRInput {

	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		Scanner sc2 = new Scanner(System.in);

		int x = sc.nextInt();
		double y = sc.nextDouble();
		String s = sc2.nextLine();
		
		System.out.println("String: "+s);
		System.out.println("Double: "+y);
		System.out.println("Int: "+x);
		
		sc.close();	
		sc2.close();
	}
	
}
