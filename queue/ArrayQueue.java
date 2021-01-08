public class ArrayQueue {
    private String[] items;
    private int n = 0;     // 数组大小
    private int head = 0;  // 头下标
    private int tail = 0;  // 队尾下标

    // 初始化
    public ArrayQueue(int n) {
        this.items = new String[n];
        this.n = n;
    }

    // 入队
    public boolean enqueue(String item) {
        // 队尾没有空间
        if (tail == n) {
            // 头部没有空间
            if (head == 0)
                return false;
            // 头部有空间，转移数据
            for (int i = head; i < tail; i++) {
                // i-head对应从0开始的下标
                items[i-head] = items[i];
            }
            // 数据转移完毕，更新head、tail
            head = 0;
            tail = tail - head;
        }
        items[tail] = item;
        tail++;
        return true;
    }

    // 出队
    public String dequeue(String item) {
        if (head == tail)
            return null;
        String temp = items[head];
        head++;
        return temp;
    }
}
