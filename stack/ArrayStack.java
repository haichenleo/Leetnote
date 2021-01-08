public class ArrayStack {
    private String[] items;
    private int count;    // 元素个数
    private int n;        // 栈的大小

    // 初始化一个大小为n的数组
    public ArrayStack(int n) {
        this.items = new String[n];
        this.count = 0;
        this.n = n;
    }

    // 入栈
    public boolean push(String str) {
        // 满空间
        if (count == n)
            return false;
        items[count] = str;
        count++;
        return true;
    }

    // 出栈
    public String pop() {
        if (count == 0)
            return null;
        String temp = items[--count];
        return temp;
    }
}
