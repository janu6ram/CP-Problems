// """Add a couple methods to our LinkedList class,
// and use that to implement a Stack.
// You have 4 functions below to fill in:
// insert_first, delete_first, push, and pop.
// Think about this while you're implementing:
// why is it easier to add an "insert_first"
// function than just use "append"?"""

class Element {
	int value;
	Element next;

	public Element(int value) {
		this.value = value;
		this.next = null;
	}
}

class LinkedList {
	Element head;

	public LinkedList(Element head) {
		this.head = head;
	}

	public void append(Element new_element) {
		Element current = this.head;
		if (this.head != null) {
			while (current.next != null) {
				current = current.next;
			}
			current.next = new_element;
		} else {
			this.head = new_element;
		}
	}

	public void insert_first(Element new_element) {
		// "Insert new element as the head of the LinkedList"
		if (head == null) {
			head = new_element;
			return;
		}
		new_element.next = head;
		head = new_element;
		// Element current = head;
		// head = new_element;
		// head.next = current;
	}

	public Element delete_first() {
		// "Delete the first (head) element in the LinkedList as return it"
		if (head == null) {
			return null;
		}
		Element current = head;
		if (head.next == null) {
			head = null;
			return current;
		}
		head = head.next;
		return current;

	}

	public String toString() {
		StringBuilder s = new StringBuilder();
		Element current = this.head;
		while (current.next != null) {
			System.out.print(current.value + " ");
			s.append(current.value + " ");
			current = current.next;
		}
		s.append(current.value);
		return s.toString();
	}
}

public class stacks {
	LinkedList ll;

	public stacks(Element top) {
		ll = new LinkedList(top);
	}

	public void push(Element e) {
		// "Push (add) a new element onto the top of the stack"
		ll.insert_first(e);
	}

	public Element pop() {
		return ll.delete_first();
	}

	public String toString() {
		return ll.toString();
	}

	public static void main(String[] args) {
		Element e1 = new Element(1);
		Element e2 = new Element(2);
		Element e3 = new Element(3);
		stacks stack = new stacks(e1);
		stack.push(e2);
		stack.push(e3);
		System.out.println(stack.toString());
	}
}
