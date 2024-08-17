from collections import deque

deque_q = deque()
for i in range(1000000) :
    deque_q.append(i)
for _ in range(10000000):
    deque_q.popleft()
print('end')

# 매우 빠른편