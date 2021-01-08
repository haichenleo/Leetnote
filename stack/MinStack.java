import java.util.Deque;
import java.util.LinkedList;

class MinStack {
    Deque<Integer> stack;
    Deque<Integer> minStack;

    public MinStack() {
        stack = new LinkedList<>();
        minStack = new LinkedList<>();
        minStack.push(Integer.MAX_VALUE); // 避免判断第一次压栈的特殊情况
    }

    public void push(int x) {
        stack.push(x);
        minStack.push(Math.min(x, minStack.peek())); // Math.min
    }

    public void pop() {
        stack.pop();
        minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}