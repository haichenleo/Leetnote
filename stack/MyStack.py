# 队列实现栈

import collections

# 单队列
class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    # 先将x入队，再将x前的所有元素出队再入队，实现
    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue