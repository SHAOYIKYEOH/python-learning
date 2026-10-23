# Data Structure（数据结构）：例如 List、Deque。
# Access Pattern（存取规则）：例如 Stack（FILO）、Queue(FIFO)。

# Python lists can be used as stacks with append() and pop().
# Python 的列表可以用作栈：从右端添加、从右端移除，后进先出。

# A deque can be used as a queue with append() and popleft().
# 双端队列可以用作普通队列：从右端添加、从左端移除，先进先出。

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(5)
print(queue)