class LinearQueue:
    def __init__(self, size):
        self.size = size  # 큐의 최대 용량 설정
        self.queue = [None] * size  # 큐를 리스트로 초기화
        self.front = self.rear = -1  # front와 rear를 -1로 초기화하여 빈 큐 상태로 설정

    # 공백상태
    def is_empty(self):
        return self.front == -1  # front가 -1이면 큐가 비어있음을 의미

    # 포화 상태
    def is_full(self):
        return self.rear == self.size - 1  #

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = self.rear = 0  # 큐가 비어있으면 front와 rear를 0으로 설정, 큐에 아이템이 하나 있으면 front와 rear는 같은 위치를 가리킴
        else:
            self.rear = self.rear + 1 # rear를 다음 위치로 이동
        self.queue[self.rear] = item  # rear 위치에 아이템 저장

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]  # front 위치의 아이템 추출
        if self.front == self.rear:
            self.front = self.rear = -1  # 큐에 아이템이 하나 남아있는 경우 front와 rear를 초기화
        else:
            self.front = self.front + 1  # front를 다음 위치로 이동
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]  # front 위치의 아이템 반환

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        i = self.front
        while i != self.rear:  # front부터 rear까지 반복하면서 아이템 출력
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size  # 다음 위치로 이동
        print(self.queue[i], end=" ")  # rear 위치의 아이템 출력
        print()



# 테스트
queue = LinearQueue(5)
queue.enqueue(1)  # rear = 0
queue.enqueue(2)  # rear = 1
queue.enqueue(3)  # rear = 2
queue.enqueue(4)  # rear = 3
queue.enqueue(5)  # rear = 4
queue.enqueue(6)  # 큐가 가득 차서 에러가 나야 합니다.

queue.display()  # 1 2 3 4 5
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2

queue.display()  # 3 4 5
print(queue.peek())  # 3

queue.dequeue()
queue.display() # 4 5
print(f'큐 포화 상태 체크: {queue.is_full()}') # True
queue.dequeue() # 4
queue.display() # 5
print(f'큐 포화 상태 체크: {queue.is_full()}') # True
queue.enqueue(6)
queue.dequeue() # 5
print(f'큐 포화 상태 체크: {queue.is_full()}') # False
queue.display() # 큐가 비어있음
queue.dequeue()  # 큐가 비어있음