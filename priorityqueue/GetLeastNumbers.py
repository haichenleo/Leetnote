# 最小的k个数

# 方法一：直接排序
# arr.sort()
# return arr[:k]

# 方法二：堆
# 用一个大顶堆维护k个最小值
# python中只有小顶堆，因此压入负数
import heapq

def getLeastNumbers(arr, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, -arr[i])
    for i in range(k, len(arr)):
        if -heap[0] > arr[i]:
            heapq.heappop(heap)
            heapq.heappush(heap, -arr[i])
    return [-i for i in heap]