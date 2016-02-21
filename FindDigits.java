import java.io.*;
import java.util.*;

public class FindDigits {

/*
HackerRank: Implementation Challenges::Find Digits
*/

	static int FindDigit(int value) {

		String valueStr = "" + value;

		int counter = 0;

		for (int i = 0; i < valueStr.length(); i++) {
			if (Character.getNumericValue(valueStr.charAt(i)) != 0
					&& value % Character.getNumericValue(valueStr.charAt(i)) == 0) {
				counter++;
			}
		}

		return counter;

	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int N = Integer.parseInt(line);

		for (int i = 0; i < N; i++) {
			System.out.println(FindDigit(Integer.parseInt(br.readLine())));
		}
	}
}
