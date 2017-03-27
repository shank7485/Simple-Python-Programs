import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class FizzBuzzClassic {
    
    static void FB(int N) {
        
        if(N == 0){
            System.out.println("0");
        }
        
		for (int i = 1; i <= N; i++) {

			if (i % 3 == 0 && i % 5 == 0) {
				System.out.println("FizzBuzz");
			}

			else if (i % 3 == 0) {
				System.out.println("Fizz");
			}

			else if (i % 5 == 0) {
				System.out.println("Buzz");
			}

			else if (i % 3 == 0 && i % 5 == 0) {
				System.out.println("FizzBuzz");
			}

			else {
				System.out.println(i);
			}
		}
	}

    public static void main(String[] args) throws IOException {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int N = Integer.parseInt(line);

		FB(N);
    }
}
