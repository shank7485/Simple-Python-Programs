
public class DetectLoop {

	class node {

		int data;
		node next;

		public node(int d) {
			data = d;
			next = null;
		}
	}

	node head = null;

	public void addToLinkedList(int d) {

		node temp = new node(d);

		if (head == null) {
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

	public void printList() {

		node current = head;

		while (current != null) {
			System.out.print(current.data + " -> ");
			current = current.next;
		}

		System.out.print("null");
		System.out.println();
	}

	public void createLoop() {

		node temp = head;
		node current = head;
		temp = temp.next;

		while (current.next != null) {
			current = current.next;
		}

		current.next = temp;
	}

	public void detectLoop() {

		//My implementation
		node slow = head;
		node fast = head.next;

		while (slow.next != null && fast.next != null) {
			if (slow.next == fast.next) {
				System.out.println("Loop Exists");
				break;
			}

			slow = slow.next;
			fast = fast.next.next;
			
			
		}
		
		System.out.println("No loop exists");
	}

	public boolean detect() {

		//Stackoverflow solution
		node slow = head;
		node fast = head;

		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;

			if (slow == fast) {
				return true;
			}
		}

		return false;

	}

	public static void main(String[] args) {

		DetectLoop object = new DetectLoop();
		object.addToLinkedList(10);
		object.addToLinkedList(20);
		object.addToLinkedList(30);
		object.addToLinkedList(40);

		object.printList();

		//object.createLoop();

		//if(object.detect())
		//	System.out.println("Loop Present");
		//else
		//	System.out.println("No Loop");
		
		object.detectLoop();

	}

}
