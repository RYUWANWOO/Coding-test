import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a,b = input().strip().split()
    a = int(a,2)
    b = int(b,2)

    tmp = format(a+b,'b')
    print(tmp)