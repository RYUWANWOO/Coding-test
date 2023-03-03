n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]

linear_data = []

for i in range(n):
    for j in range(n):
        linear_data.append(data[i][j])

linear_data.sort(reverse=True)
print(linear_data[n-1])


