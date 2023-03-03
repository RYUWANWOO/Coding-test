t = int(input())

for _ in range(t):
    n = int(input())

    data = list(map(int,input().split()))
    data.sort()

    result = [0] * n
    idx = -1
    for i in range(n):
        if i % 2 == 0:
            result[i//2] = data[i]
        else:
            result[idx] = data[i]
            idx -= 1



    diff = []
    for i in range(n-1):
        diff.append(abs(result[i]-result[i+1]))

    diff.append(abs(result[0]-result[-1]))

    print(max(diff))

