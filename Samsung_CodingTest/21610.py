import sys
input = sys.stdin.readline
from collections import deque

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
N,M = map(int,input().split())
cloud_map = [list(map(int,input().split())) for _ in range(N)]

#초기 구름의 위치를 저장하자.
cloud_position = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])
def copy_water(cloud_map,x,y):
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]

    count = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N  or ny >= N:
            continue
        if cloud_map[nx][ny] != 0:
            count += 1
    cloud_map[x][y] += count

def move_cloud(visited,unchanged_cloud,cloud_map,cloud_position,dir,s):
    global N
    for cloudPos in cloud_position:
        x,y = cloudPos
        nx = (x + s*dx[dir]) % N
        ny = (y + s*dy[dir]) % N
        #비를 내리자
        cloud_map[nx][ny] += 1
        #구름의 위치
        visited[nx][ny] = 1
        #비를 복사해버려
        unchanged_cloud.append((nx,ny))
    for nx,ny in unchanged_cloud:
        copy_water(cloud_map, nx, ny)

def make_cloud(visited,clound_map,cloud_position):
    for i in range(N):
        for j in range(N):
            if clound_map[i][j] >= 2 and visited[i][j] != 1:
                #이자리 다시 릴리즈
                visited[i][j] = 0
                #구름을 만들고
                cloud_map[i][j] -= 2
                #구름의 위치를 저장하자
                cloud_position.append((i,j))

result = 0
#구름 이동 방향정보 입력
for _ in range(M):
    #방향과 이동 거리
    visited = [[0] * N for _ in range(N)]
    unchanged_cloud = deque([])
    d,s = map(int,input().split())
    move_cloud(visited,unchanged_cloud,cloud_map,cloud_position,d-1,s)
    cloud_position.clear()
    make_cloud(visited,cloud_map,cloud_position)
    unchanged_cloud.clear()



for c_m in cloud_map:
    result += sum(c_m)
print(result)
