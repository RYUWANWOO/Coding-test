import sys
input = sys.stdin.readline

N = int(input())
find_num = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = [[0 for _ in range(N)] for _ in range(N)]

x,y = N//2, N//2
number = 2

outer_count = 2
inner_count = 1
direction = 0

graph[x][y] = 1
flag = False

while True:
    if flag:
        break

    for i in range(outer_count):
        for j in range(inner_count):
            x = x + dx[direction % 4]
            y = y + dy[direction % 4]

            graph[x][y] = number
            number += 1

            if number == N**2+1:
                flag = True
                break

        direction += 1
        if flag:
            break

    inner_count += 1

for g in graph:
    print(*g)

for i in range(N):
    for j in range(N):
        if graph[i][j] == find_num:
            print(i+1, j+1)