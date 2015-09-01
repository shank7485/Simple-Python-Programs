
public class BubbleSort {

	public static void main(String[] args){
		
		int array[] = {3,4,2,1,5};
		
		for(int i = 0; i < array.length - 1; i++){
			
			for(int j = 0; j <array.length - 1;j++){
								
				if(array[j]>array[j+1]){
					
					int temp = array[j+1];
					array[j] = array[j+1];
					array[j] = temp;
				}
				
			}
		}
		
		
	System.out.println(array[4]);	
	}
	
}
