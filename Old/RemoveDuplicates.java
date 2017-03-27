import java.util.ArrayList;
import java.util.Hashtable;

class RemoveDuplicates {

	class node {

		int data;
		node next;

	}

	node head = null;

	public void addtoList(int data) {

		node temp = new node();
		temp.next = null;
		temp.data = data;

		if(head == null){
			head = temp;
		}
		
		else {
			node current = head;
			while (current.next != null) {
				current = current.next;
			}

			current.next = temp;
		}
		

	}

	public void delete(node head, int data) {

		node current = head;
		while (current != null) {
			if (current.next.data == data) {
				current.next = current.next.next;
			}

			else {
				current = current.next;
			}
		}

	}

	public boolean Check(ArrayList<Integer> A, int data) {

		for (int i = 0; i < A.size(); i++) {
			if (A.get(i) == data) {
				return true;
			}
		}

		return false;

	}

	public void deleteDuplicates(node head, int data) {
    //O(n^2)
		node current = head;
		node prev_temp = null;

		ArrayList<Integer> A = new ArrayList<>();

		while (current.next != null) {
			if (current.data == data) {
				if (Check(A, data) == false) {
					A.add(current.data);
				}

				else {
					prev_temp.next = current.next;
				}
			}

			prev_temp = current;
			current = current.next;
		}

	}

	public void deleteDuplicateUsingHashTable(node head) {
	  // O(n)
		Hashtable table = new Hashtable();
		node current = head;
		node temp_prev = null;

		while (current.next != null) {
			if (table.containsKey(current.data)) {
				temp_prev.next = current.next;
			}

			else {
				table.put(current.data, true);
				temp_prev = current;
			}

			current = current.next;
		}
	}

	public void printList(node head) {

		node current = head;

		while (current.next != null) {
			System.out.print(current.data + " -> ");
			current = current.next;
		}

		System.out.print(current.data + " -> ");
		System.out.print("null");
		System.out.println();

	}

	public static void main(String[] args) {

		RemoveDuplicates object = new RemoveDuplicates();
		object.addtoList(10);
		object.addtoList(10);
		object.addtoList(20);
		object.addtoList(20);
		object.addtoList(20);
		object.addtoList(30);
		object.addtoList(30);
		object.addtoList(30);
		object.addtoList(10);
		object.addtoList(20);

		object.printList(object.head);

		
		object.deleteDuplicateUsingHashTable(object.head);
		object.printList(object.head);
    //still has some bugs
	}

}
