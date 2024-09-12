from collections import deque



def calculate (num, type) :

    if type == 1 :
        num += 1

    if type == 1:
        num -= 1

    if type == 1 :
        num *= 2

    if type == 1 :
        num -= 10

def bfs(num) :

    queue = deque([(num)])





T = int(input())

for test_case in range (1, T + 1) :
    N, M = map(int,input().split())