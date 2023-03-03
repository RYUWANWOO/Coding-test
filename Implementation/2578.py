import sys
input = sys.stdin.readline


def check_bingo(visited):
    cnt = 0
    #가로 체크
    for i in range(5):
        if all(visited[i]):
            cnt += 1
    #세로 체크
    for i in range(5):
        if visited[0][i] and visited[1][i] and visited[2][i] and visited[3][i] and visited[4][i]:
            cnt += 1
    #대각 체크
    if visited[0][0] and visited[1][1] and visited[2][2] and visited[3][3] and visited[4][4]:
        cnt += 1

    if visited[0][4] and visited[1][3] and visited[2][2] and visited[3][1] and visited[4][0]:
        cnt += 1

    return cnt


def find_pos(graph,num):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == num:
                return i,j

graph = [list(map(int,input().split())) for _ in range(5)]

query = [list(map(int,input().split())) for _ in range(5)]

visited = [[False for _ in range(5)] for _ in range(5)]

count = 1
for i in range(5):
    for j in range(5):
        x,y = find_pos(graph,query[i][j])
        visited[x][y] = True
        if check_bingo(visited) >= 3:
            print(count)
            exit()
        count += 1
