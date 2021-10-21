import java.util.Queue;
import java.util.Stack;

/**
 * Make a queue from two Stacks
 */

class QueueStack<T> {
    private Stack<T> inbox = new Stack<T>();
    private Stack<T> outbox = new Stack<T>();

    public boolean isEmpty() {
        return inbox.isEmpty() && outbox.isEmpty();
    }

    public void enqueue(T item) {
        inbox.push(item);
    }

    public T dequeue() {
        if (outbox.isEmpty()) {
            while (!inbox.isEmpty()) {
                outbox.push(inbox.pop());
            }
        }
        return outbox.pop();
    }
}

public class queues_from_stack {
    public static void main(String[] args) {
        System.out.println("Hello World");
        QueueStack<Integer> q = new QueueStack<Integer>();
        q.enqueue(5);
        q.enqueue(6);
        q.enqueue(7);

        while (!q.isEmpty()) {
            System.out.println(q.dequeue());
        }
        q.enqueue(9);
        q.enqueue(10);

        while (!q.isEmpty()) {
            System.out.println(q.dequeue());
        }
    }
}