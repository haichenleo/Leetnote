# LRU - Least Recently Used

# 双链表 + 哈希表
class LRUCache:
    # 内部类，双向链表节点
    class DLinkedNode:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cache = dict()
        # dummy node
        self.head = self.DLinkedNode()
        self.tail = self.DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity   # 链表容量
        self.size = 0              # 当前节点数量
        # 特殊处理
        if self.capacity < 1:
            raise Exception('Capacity less than 1')

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果存在，通过hash定位链表位置，再将node移动到表头，并返回值
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 如果已存在，更新值，并移到表头
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        # 不存在，则新建node，并插入到表头
        else:
            node = self.DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1  # size +1
            self.checkToRemove() # 检查并移除尾节点

    def moveToHead(self, node):
        # 先将node从链表中移除，再插到表头
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        # 从链表中移除node
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def addToHead(self, node):
        # 将node插入链表头
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node

    def checkToRemove(self):
        # 检查，移除尾结点，size-1，移除哈希表键值对
        if self.size > self.capacity:
            removed = self.removeTail()
            self.size -= 1
            self.delFromDict(removed)

    def removeTail(self):
            node_to_delete = self.tail.prev
            self.removeNode(node_to_delete)
            return node_to_delete

    def delFromDict(self, node):
        if node.key not in self.cache:
            return 
        self.cache.pop(node.key)



lruCache = LRUCache(2)
lruCache.put(2,1)
lruCache.put(2,2)
print(lruCache.get(2))
lruCache.put(1,1)
lruCache.put(4,1)
print(lruCache.get(2))

