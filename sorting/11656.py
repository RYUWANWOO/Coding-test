result = []

strstr = input()

for i in range(len(strstr)):
    result.append(strstr[i:])

result.sort()

for r in result:
    print(r)