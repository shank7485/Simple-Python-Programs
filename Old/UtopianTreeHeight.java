import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UtopianTreeHeight {

/*
HackerRank: Utopian Tree
*/

	static int TreeHeight(int cycle) {
		int height = 1;
		if (cycle % 2 == 0) {
			for (int i = 0; i < cycle / 2; i++) {
				height = 2 * height + 1;
			}
		}

		else {
			for (int i = 0; i < (cycle / 2) + 1; i++) {
				height = 2 * height + 1;
			}
			height = height - 1;
		}

		return height;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int N = Integer.parseInt(line);

		for (int i = 0; i < N; i++) {
			System.out.println(TreeHeight(Integer.parseInt(br.readLine())));
		}
	}
}
