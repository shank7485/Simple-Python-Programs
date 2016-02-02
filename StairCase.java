import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StairCase {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        for(int i = 1; i <= n; i++){
            
            String buffer = "";
                for(int k = 1; k <= n - i; k++){
                    buffer = buffer + " ";
                }
            
            for(int j = 1; j <= i; j++){
                buffer = buffer + "#";    
            }
            System.out.println(buffer);
        }
    }
}
