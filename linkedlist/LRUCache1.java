import java.util.HashMap;

class LRUCache {

    class Node {
        private int key, val;
        private Node next, prev;
        public Node(){}
        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    class DLinkList {
        private int size;
        private Node head, tail;
        public DLinkList() {
            head = new Node();
            tail = new Node();
            head.next = tail;
            tail.prev = head;
            this.size = 0;
        }

        public void addToHead(Node node) {
            node.next = head.next;
            node.prev = head;
            head.next.prev = node;
            head.next = node;
            size ++;
        }

        public void removeNode(Node node) {
            node.prev.next = node.next;
            node.next.prev = node.prev;
            size --;        }

        public int size() {
            return this.size;
        }
    }

    private HashMap<Integer, Node> cache;
    private DLinkList list;
    private int capacity;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.list = new DLinkList();
    }

    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        Node node = this.cache.get(key);
        this.list.removeNode(node);
        this.list.addToHead(node);
        return node.val;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.val = value;
        } else {
            Node node = new Node(key, value);
            this.cache.put(key, node);
            this.list.addToHead(node);
            this.list.size ++;
            if (this.list.size() > this.capacity) {
                this.list.removeNode(this.tail.prev);
            }
        }
    }

}