import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
k = int(input())
my_map = [[0] * n for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

direction_queue = deque([])

for _ in range(k):
    r,c = map(int,input().split())
    my_map[r-1][c-1] = 1

l = int(input())

for _ in range(l):
    t,d = input().split()
    direction_queue.append((int(t),d))


dir = 0
time = 0
x,y = 0,0
my_map[x][y] = 2
change_time,change_direction = direction_queue.popleft()
#꼬리정보 가지고 있어야함
tail_x,tail_y = 0,0
head_dir = deque([])
while True:
    #시간 1초 증가
    time += 1

    if time == change_time+1:
        if change_direction == 'L':
            dir = (dir - 1) % 4
        elif change_direction == 'D':
            dir = (dir + 1) % 4
        if direction_queue:
            change_time, change_direction = direction_queue.popleft()



    nx = x + dx[dir]
    ny = y + dy[dir]

    #사과를 먹으면
    if 0<=nx<n and 0<=ny<n and my_map[nx][ny] == 1:
        my_map[nx][ny] = 2
        head_dir.append((dx[dir],dy[dir]))
        x,y = nx,ny
        continue
    #사과가 아니면
    if 0<=nx<n and 0<=ny<n and my_map[nx][ny] == 0:
        #머리를 앞으로 늘리고
        my_map[nx][ny] = 2
        head_dir.append((dx[dir],dy[dir]))
        #꼬리를 줄인다.
        my_map[tail_x][tail_y] = 0
        d_tail_x,d_tail_y = head_dir.popleft()
        tail_x += dx[d_tail_x]
        tail_y += dx[d_tail_y]

        x,y = nx,ny
        continue

    if (nx < 0 or ny < 0 or nx >= n or ny >= n) or my_map[nx][ny] == 2:
        break



print(time)