import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

count = 0
N, M = map(int, input().split())
r, c, d = map(int, input().split())
cleaning_map = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def go(x, y, d):
    global count

    dir = d
    for i in range(4):
        dir = (dir + 3) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 1 or nx > N or ny < 1 or ny > M:
            continue
        if cleaning_map[nx][ny] == 1:
            continue

        if cleaning_map[nx][ny] == 0:
            cleaning_map[nx][ny] = 2
            count += 1
            go(nx, ny, dir)
            return

    # 뒤로 가야 되닌깐

    dir = (dir + 2) % 4
    nx = x + dx[dir]
    ny = y + dy[dir]

    if cleaning_map[nx][ny] == 1:
        return
    else:
        go(nx, ny, d)


count = 1
cleaning_map[r][c] = 2
go(r, c, d)
print(count)