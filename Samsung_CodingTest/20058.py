import sys
input = sys.stdin.readline
from collections import deque
#input
n,q = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(2**n)]
query = list(map(int,input().split()))

row_N = 2**n

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False] * row_N for _ in range(row_N)]

def bfs(graph,x,y):
    queue = deque([])
    queue.append((x,y))
    visited[x][y] = True

    count = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= row_N or ny >= row_N:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] > 0 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                count += 1

    return count

def rotation(graph,L):
    global row_N
    partition_num = 2**L

    result = [[0]*row_N for _ in range(row_N)]

    for i in range(0,row_N,partition_num):
        for j in range(0,row_N,partition_num):
            for r in range(partition_num):
                for c in range(partition_num):
                    result[i+c][j+partition_num-1-r] = graph[i+r][j+c]

    return result


def remain(graph):

    melting_list = []
    for x in range(row_N):
        for y in range(row_N):
            count = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny <0 or nx >= row_N or ny >= row_N:
                    continue
                elif graph[nx][ny] > 0 :
                    count+=1

            if graph[x][y] > 0:
                if count < 3:
                    melting_list.append((x,y))

    for m in melting_list:
        x,y = m
        graph[x][y] -= 1

    return graph


for l in query:
    graph = rotation(graph,l)
    graph = remain(graph)

result = []
for i in range(row_N):
    for j in range(row_N):
        if graph[i][j] > 0 and not visited[i][j]:
           result.append(bfs(graph,i,j))

sum_val = 0

for i in range(row_N):
    sum_val += sum(graph[i])

print(sum_val)
if result:
    print(max(result))
else:
    print(0)
#print(max(result))

