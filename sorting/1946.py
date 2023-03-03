t = int(input())

for _ in range(t):
    n = int(input())
    ranking = []
    for _ in range(n):
        a, b = map(int, input().split())
        ranking.append([a, b])

    ranking.sort()
    cnt = 1
    temp = ranking[0][1]

    for i in range(1,len(ranking)):
        if temp > ranking[i][1]:
            cnt += 1
            temp = ranking[i][1]

    print(cnt)
