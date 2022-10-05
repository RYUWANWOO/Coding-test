import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    input()
    m_list = list(map(int,input().split()))
    print(min(m_list),max(m_list))
