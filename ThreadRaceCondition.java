public class ThreadRaceCondition implements Runnable {

	int data;
	int count;

	public ThreadRaceCondition(int data, int count) {
		this.data = data;
		this.count = count;
	}

	public void run() {
		func1(this.data, this.count);
		func2(this.data, this.count);
	}

	void func1(int data, int count) {

		for (int i = 0; i < count; i++) {
			this.data++;
		}

		System.out.println(this.data);

	}

	synchronized void func2(int data, int count) {

		for (int i = 0; i < count; i++) {
			this.data++;
		}
		System.out.println(this.data);

	}

	public static void main(String[] args) {
		int globalInt = 0;

		ThreadRaceCondition obj = new ThreadRaceCondition(globalInt, 100);
		Thread thread_1 = new Thread(obj);
		Thread thread_2 = new Thread(obj);
		thread_1.start();
		thread_2.start();
	}
}
