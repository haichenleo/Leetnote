import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [math.inf]  # math.inf = float('inf) 浮点正无穷大

    def push(self, x:int) -> None:
        self.stack.append(x)
        # 在x入栈的同时，用最小栈记录当前的最小值
        # 第一次压栈时和无穷大比较，最小值为x
        self.minStack.append(min(x,self.minStack[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop() # minstack跟着出栈，移除当前最小值
        return None
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        return self.minStack[-1]

# 不能用一个常量 minValue 保存最小值，
# 因为如果 minValue 对应的元素被pop出去，
# minValue无法更新
        