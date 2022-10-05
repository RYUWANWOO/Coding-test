import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

path = deque([])

def snail(n):
    row = 0 #2
    col = -1 #2
    cnt = 1 #3
    trans = 1 #4
    while n > 0: #5
        for i in range(n): #6
            col += trans
            path.appendleft((row,col))
        n -= 1 #7
        for j in range(n): #8
            row += trans
            path.appendleft((row,col))
            cnt += 1
        trans *= -1 #9
snail(N)
print(path)