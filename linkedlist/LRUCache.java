import java.util.HashMap;
import java.util.Map;

/**
 * LRUCache
 */
public class LRUCache {

    // 内部类
    class DLinkNode {
        int key;
        int value;
        DLinkNode prev;
        DLinkNode next;
        public DLinkNode(){}
        public DLinkNode(int key, int value){
            this.key = key;
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }

    private Map<Integer, DLinkNode> cache;
    private int size, capacity;
    private DLinkNode head, tail;
    
    // 构造器
    public LRUCache(int capacity) {
        this.cache = new HashMap<Integer, DLinkNode>();
        this.size = 0;
        this.capacity = capacity;
        this.head = new DLinkNode();
        this.tail = new DLinkNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    public int get(int key) {
        if (!this.cache.containsKey(key)) {
            return -1;
        }
        DLinkNode node = this.cache.get(key);
        // 移动到头结点
        moveToHead(node);
        return node.value;
    }

    private void moveToHead(LRUCache.DLinkNode node) {
        removeNode(node);
        addToHead(node);
    }

    private void addToHead(LRUCache.DLinkNode node) {
        node.next = this.head.next;
        node.prev = node.next.prev;
        node.next.prev = node;
        this.head.next = node;
    }

    private void removeNode(LRUCache.DLinkNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.next = null;
        node.prev = null;
    }

    public void put(int key, int value) {
        if (this.cache.containsKey(key)) {
            DLinkNode node = this.cache.get(key);
            node.value = value;
            moveToHead(node);
            return;
        }
        DLinkNode newNode = new DLinkNode(key, value);
        addToHead(newNode);
        this.cache.put(key, newNode);
        this.size ++;
        checkToRemove();
    }

    private void checkToRemove() {
        if (!(this.size > this.capacity))
            return;
        DLinkNode nodeToRemove = this.tail.prev;
        removeNode(nodeToRemove);
        this.size --;
        this.cache.remove(nodeToRemove.key);
    }

    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.get(1)); 
    }
}