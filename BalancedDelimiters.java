import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BalancedDelimiters {

	/*
	 * HackerRank: BalancedDelimiters
	 * () = 1 [] = 2 {} = 3
	 */

	static boolean isPalindrome(String str) {
		// ([{}])
		// 123321
		int n = str.length();
		String number = "";

		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == '(' | str.charAt(i) == ')') {
				number = number + "1";
			}

			else if (str.charAt(i) == '[' | str.charAt(i) == ']') {
				number = number + "2";
			}

			else if (str.charAt(i) == '{' | str.charAt(i) == '}') {
				number = number + "3";
			}

		}
		for (int i = 0; i < n / 2; i++) {
			if (number.charAt(i) != number.charAt(n - i - 1)) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		/*
		 * Enter your code here. Read input from STDIN. Print output to STDOUT.
		 * Your class should be named Solution.
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		if (isPalindrome(line))
			System.out.println("True");
		else
			System.out.println("False");
	}

}
