import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MyHashMap {
    private int space;
    private List<Bucket> hash_table;

    public MyHashMap() {
        this.space = 2069;
        hash_table = new ArrayList<Bucket>();
        // 数组初始化
        for (int i = 0; i < this.space; i++) {
            hash_table.set(i, new Bucket());
        }
    }

    public int hash(int key) {
        return key % this.space;
    }

    public void put(int key, int value) {
        int hash_key = this.hash(key);
        this.hash_table.get(hash_key).update(key, value);
    }

    public int get(int key) {
        int hash_key = this.hash(key);
        return this.hash_table.get(hash_key).get(key);
    }

    public void remove(int key) {
        int hash_key = this.hash(key);
        this.hash_table.get(hash_key).remove(key);
    }

    
}

// 存储一对数据，元组
class Pair<U, V> {
    public U first;
    public V second;

    public Pair(U first, V second) {
        this.first = first;
        this.second = second;
    }
}

class Bucket {
    private List<Pair<Integer, Integer>> bucket;

    public Bucket() {
        bucket = new LinkedList<Pair<Integer, Integer>>();
    }

    public Integer get(Integer key) {
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first == key)
                return pair.second;
        }
        return -1;
    }

    public void update(Integer key, Integer value) {
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first == key)
                pair.second = value;
                return;
        }
        this.bucket.add(new Pair<Integer, Integer>(key, value));
    }

    public void remove(Integer key) {
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first == key)
                bucket.remove(pair);
                break;
        }
    }
}
