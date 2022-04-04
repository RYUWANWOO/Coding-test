import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

#N은 맵 크기 M은 꼭 있어야 할 치킨집의 수
N,M = map(int,input().split())

chicken_store = deque([])
home = deque([])

temp = [list(map(int,input().split())) for _ in range(N)]

def calc_distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

#좌표 입력
for i in range(N):
    for j in range(N):
        if temp[i][j] == 1:
            home.append((i,j))
        elif temp[i][j] ==2:
            chicken_store.append((i,j))

min_val = int(1e9)

for ck_store in combinations(chicken_store,M):

    total = 0
    for h in home:
        min_chicken = 99999
        for s in ck_store:
            min_chicken = min(min_chicken,calc_distance(h,s))
        total += min_chicken

    min_val = min(min_val,total)

print(min_val)


