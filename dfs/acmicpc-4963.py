import sys
from collections import deque

input = sys.stdin.readline

def print_map(graph):
    for g in graph:
        print(g)
    print()

def bfs(graph,x,y):
  dx = [-1,1,0,0,-1,1,-1,1]
  dy = [0,0,-1,1,-1,-1,1,1]
  
  graph[x][y] = 0
  
  queue = deque([])
  queue.append((x,y))
  
  
  while queue:
    x,y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or ny<0 or nx>=h or ny>=w:
        continue
      if graph[nx][ny] == 0:
        continue 
      if graph[nx][ny] == 1:
        queue.append((nx,ny))
        graph[nx][ny] = 0

while True:
    w,h = map(int,input().split())
    count = 0
    if w == 0 and h == 0:
        break
    graph = [list(map(int,input().split())) for i in range(h)]
    for i in range(h):
      for j in range(w):
        if graph[i][j] == 1:
          bfs(graph,i,j)
          count += 1
    print(count)
    
