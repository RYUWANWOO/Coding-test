import sys

input = sys.stdin.readline

m_str = list(input().strip())

i, start = 0,0

while i <len(m_str):
    if m_str[i] == "<":
        i += 1
        while m_str[i] != ">":
            i += 1
        i += 1
    elif m_str[i].isalnum():
        start = i
        while i < len(m_str) and m_str[i].isalnum():
            i += 1
        tmp = m_str[start:i]
        tmp.reverse()
        m_str[start:i] = tmp
    else:
        i += 1

print("".join(m_str))

