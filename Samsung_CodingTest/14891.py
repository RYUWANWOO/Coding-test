import sys
input = sys.stdin.readline
from collections import deque
CogWheel = deque([deque(list(map(int, input().strip()))) for _ in range(4)])


def calc_score(CogWheel):
    result = 0
    for i in range(4):
        result += (CogWheel[i][0] * pow(2,i))

    return result

#돌릴횟수
#회전 방향: 1->시계 방향 -1->반시계 방향
K = int(input())
for _ in range(K):
    num, rot_dir = map(int, input().split())
    #인덱스가 1차이 나므로
    num -= 1
    #loop돌면서 좌우 체크
    affect = []
    cnt = 0
    for idx in range(num,0,-1):
        if CogWheel[idx][-2] != CogWheel[idx-1][2]:
            cnt += 1
            affect.append((idx-1,rot_dir*pow(-1,cnt)))
        else:
            break
    cnt = 0
    for idx in range(num,3,1):
        if CogWheel[idx][2] != CogWheel[idx+1][-2]:
            cnt += 1
            affect.append((idx+1, rot_dir * pow(-1,cnt)))
        else:
            break

    #영향받는 걸 체크 햇으면 실제로 돌아야하는거 하고 돌리면 댐
    if rot_dir == -1:
        temp = CogWheel[num].popleft()
        CogWheel[num].append(temp)
    else:
        temp = CogWheel[num].pop()
        CogWheel[num].appendleft(temp)

    for a in affect:
        a_num,a_rotDir = a
        if a_rotDir == -1:
            temp = CogWheel[a_num].popleft()
            CogWheel[a_num].append(temp)
        else:
            temp = CogWheel[a_num].pop()
            CogWheel[a_num].appendleft(temp)

print(calc_score(CogWheel))

