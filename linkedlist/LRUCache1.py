class LRUCache1:
    """
    LRU Cache - Least Recently Used
    双链表 + 哈希表
    链表结点存储 key + value + 头尾指针
    哈希表存储 key + (K, V)
    """

    # 内部类，双端队列Node
    class DLinkNode:

        def __init__(self, key=0, value=0, prev=None, next=None) -> None:
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int) -> None:
        # 哈希表
        self.cache = dict()
        # 链表容量与node数量
        self.capacity = capacity
        self.size = 0
        # 头尾 dummy node
        self.head = self.DLinkNode()
        self.tail = self.DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        # capacity 初始值 < size, 抛出异常
        if self.capacity < self.size:
            raise Exception('capacity less than size')

    def get(self, key: int) -> int:
        # key是否存在
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 移动到头结点
        self.moveToHead(node)
        return node.value

    def put(self, key=int, value = int):
        # 已存在，更新并移动到头结点
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
            return
        # 否则新建结点，插入哈希表，并插入到头结点
        node = self.DLinkNode(key, value)
        self.cache[key] = node
        self.addToHead(node)
        self.size += 1  # size + 1
        # 检查并移除 LRU 结点
        self.checkToRemove()

    def moveToHead(self, node):
        # 从链表中移除
        self.removeNode(node)
        # 插入到头结点
        self.addToHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = node.next.prev
        node.next.prev = node
        self.head.next = node

    def checkToRemove(self):
        if self.size > self.capacity:
            removed = self.removeTail()
            self.removeDict(removed)
            self.size -= 1

    def removeTail(self):
        node_to_remove = self.tail.prev
        self.removeNode(node_to_remove)
        return node_to_remove
        
    def removeDict(self, node):
        self.cache.pop(node.key)

lruCache = LRUCache1(2)
lruCache.put(2,1)
lruCache.put(2,2)
print(lruCache.get(2))
lruCache.put(1,1)
lruCache.put(4,1)
print(lruCache.get(2))
