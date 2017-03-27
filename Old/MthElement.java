import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MthElement {

	/*
	 * 
	 * HackerRank Interview Prep
	 */
	
	class node {
		int data;
		node next = null;

		node(int data) {
			this.data = data;
		}

	}

	node root = null;

	void addToList(int data) {

		node temp = new node(data);

		if (root == null) {
			root = temp;
		}

		else {
			node current = root;
			while (current.next != null) {
				current = current.next;
			}
			current.next = temp;
		}
	}

	void traverse(int position) {
		int count = 0;
		int length = 0;
		node current = root;

		while (current != null) {
			count++;
			current = current.next;
		}

		length = count;
		int NewPosition = length - position;

		count = 0;
		current = root;

		while (current != null) {
			if (NewPosition >= 0 && position > 0) {
				if (count == NewPosition) {
					System.out.println(current.data);
				}

				count++;
				current = current.next;
			}

			else if (NewPosition < 0 | position <= 0) {
				System.out.println("NIL");
				break;
			}

		}

	}

	void print() {
		node current = root;
		while (current != null) {
			System.out.print(current.data + " -> ");
			current = current.next;
		}
		System.out.print("nil");
		System.out.println();
	}

	public static void main(String[] args) throws IOException {

		MthElement obj = new MthElement();

		BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));
		BufferedReader br2 = new BufferedReader(new InputStreamReader(System.in));

		String line1 = br1.readLine();
		String line2 = br2.readLine();

		int input1 = Integer.parseInt(line1);
		String[] number = line2.split(" ");

		for (int i = 0; i < number.length; i++) {

			obj.addToList(Integer.parseInt(number[i]));

		}

		obj.traverse(input1);

	}

}
