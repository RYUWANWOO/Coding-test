import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def rotate():
    for i in range(min(n,m)//2):
        #첫번째 좌표 저ㅇ
        s_x,s_y = i,i
        s_value = board[s_x][s_y]

        #좌
        for j in range(i+1,n-i):
            s_x = j
            prev_value = board[s_x][s_y]
            board[s_x][s_y] = s_value
            s_value = prev_value

        #하
        for j in range(i+1,m-i):
            s_y = j
            prev_value = board[s_x][s_y]
            board[s_x][s_y] = s_value
            s_value = prev_value

        #우
        for j in range(i+1,n-i):
            s_x = n-j-1
            prev_value = board[s_x][s_y]
            board[s_x][s_y] = s_value
            s_value = prev_value

        for j in range(i+1,m-i):
            s_y = m-j-1
            prev_value = board[s_x][s_y]
            board[s_x][s_y] = s_value
            s_value = prev_value

for _ in range(r):
    rotate()

for b in board:
    print(*b)
