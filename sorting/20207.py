n = int(input())

data = []
for _ in range(n):
    a,b = map(int,input().split())
    data.append([a,b])

data.sort()

start_day = data[0][0]
end_day = data[-1][1]

calendar_table = [0] * (366)

for d in data:
    s,e = d
    for i in range(s,e+1):
        calendar_table[i] += 1

row,col,ans = 0,0,0

for i in range(366):
    if calendar_table[i] != 0:
        row = max(row,calendar_table[i])
        col += 1
    else:
        ans += row * col
        row = 0
        col = 0


print()