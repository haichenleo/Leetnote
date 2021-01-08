# 循环队列的实现


# 方法一：数组
# 利用数组虚拟一个环
# tail = (head + count - 1) mod capacity
# count - 队列长度
# capacity - 数组长度
class CircularQueue1:
    
    def __init__(self, k:int):
        self.queue = [0] * k   # 初始化数组模拟循环队列
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value:int) -> bool:
        # 数组没有额外空间
        if self.count == self.capacity:
            return False
        # 计算队尾位置，令queue[tail] = value
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        # head指针向后移动一位
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def rear(self) -> int:
        if self.count == 0:
            return -1
        # 计算队尾指针前一个位置
        return self.queue[(self.headIndex + self.count -1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

# 改进：线程安全
# 以 enQueue() 为例
from threading import Lock

class CircularQueue1Lock:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        # 锁
        self.queueLock = Lock()

    def enQueue(self, value:int) -> bool:
        # 自动加锁
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity]
            self.count += 1
        # 自动释放锁
        return True

    
# 数组的另一种实现
# 同时保存 head 和 tail，用于判定队列长度
class MyCircularQueue2:

    def __init__(self, k: int):
        # 数组容量+1用于辅助计算
        self.queue = [0] * (k + 1)
        # 记录数组长度
        self.n = k + 1
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        # tail向后移动一位
        self.tail = (self.tail + 1) % self.n
        return True

    def deQueue(self) -> bool:
        if (self.head == self.tail):
            return False
        # head向后移动一位
        self.head = (self.head + 1) % self.n
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # tail对应的位置是空，返回tail-1所在的元素
        return self.queue[(self.tail - 1) % self.n]

    def isEmpty(self) -> bool:
        # head和tail重合时队列为空
        if self.head == self.tail:
            return True
        return False

    def isFull(self) -> bool:
        # head和tail位置差一位时，队列满
        if (self.tail + 1) % self.n == self.head:
            return True
        return False

    
        
# 方法二：单链表
class CircularQueue3:

    # 内部Node类
    class Node:
        def __init__(self, value, nextNode=None):
            self.value = value
            self.next = nextNode
        
    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value):
        # 判断是否有空间
        if self.capacity == self.count:
            return False
        
        # 链表为空
        if self.count == 0:
            self.head = self.Node(value)
            self.tail = self.head
        # 链表不为空
        else:
            self.tail.next = self.Node(value)
            self.tail = self.tail.next
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.value  


    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.capacity:
            return True
        return False
        