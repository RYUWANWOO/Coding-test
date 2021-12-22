import sys
from collections import deque

input = sys.stdin.readline

def print_graph(graph):
  for g in graph:
    print(g)
  print()

def bfs(graph,x,y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  v_count = 0
  o_count = 0

  if graph[x][y] == 'v':
    v_count += 1
  elif graph[x][y] == 'o':
    o_count += 1
  
  graph[x][y] = '#'

  queue = deque([])
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny<0 or nx>=r or ny>=c: #영역을 벗어 났을 때
        continue
      if graph[nx][ny] == '#': #울타리 일 때
        continue 
      if graph[nx][ny] == 'o': #양일 때
        o_count += 1
        queue.append((nx,ny))
        graph[nx][ny] = '#'
      if graph[nx][ny] == 'v': #늑대 일때
        v_count += 1
        queue.append((nx,ny))
        graph[nx][ny] = '#'
      if graph[nx][ny] == '.':
        queue.append((nx,ny))
        graph[nx][ny] = '#'
  
  if o_count > v_count:
    return o_count,0
  else:
    return 0,v_count 

r,c = map(int,input().split())
graph = [list(input().rstrip()) for i in range(r)]

#print_graph(graph)

area_o_count,area_v_count = 0,0

for i in range(r):
  for j in range(c):
    if graph[i][j] != '#':
      temp_o,temp_v = bfs(graph,i,j)
      #print_graph(graph)
      area_o_count += temp_o
      area_v_count += temp_v
    
print(area_o_count,area_v_count)
