import java.util.LinkedList;

/**
 * MyHashSet
 */
class MyHashSet {
    private int keyRange;
    private Bucket[] bucketArray;

    public MyHashSet() {
        keyRange = 769;
        bucketArray = new Bucket[this.keyRange];
        for (int i = 0; i < this.keyRange; i++) {
            bucketArray[i] = new Bucket();
        }
    }

    protected int _hash(int key) {
        return (key%this.keyRange);
    }

    public boolean contains(int key) {
        int index = this._hash(key);
        return this.bucketArray[index].exists(key);
    }

    public void add(int key) {
        int index = this._hash(key);
        this.bucketArray[index].insert(key);
    }

    public void remove(int key) {
        int index = this._hash(key);
        this.bucketArray[index].delete(key);
    }
}

/**
 * Bucket class
 */
class Bucket {
    private LinkedList<Integer> container;

    public Bucket(){
        container = new LinkedList<>();
    }

    public void insert(Integer key) {
        if (exists(key) == false){
            container.addFirst(key);
        }
    }

    public boolean exists(Integer key) {
        int index = container.indexOf(key);
        return (index != -1);
    }

    public void delete(Integer key) {
        container.remove(key);
    }
}