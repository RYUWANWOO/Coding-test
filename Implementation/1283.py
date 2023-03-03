import sys

input = sys.stdin.readline

N = int(input())

shortcut = {}
mapping = {}
data = []


for i in range(N):
    flag = False
    tmp = input().strip()
    data.append(tmp)
    words = list(tmp.split())

    temp = []
    for word in words:
        if word[0].lower() not in shortcut:
            temp.append(word[:word.index(word[0])] + "[" + word[0] + "]" + word[word.index(word[0]) + 1:])
            mapping[i] = word[0].lower()
            flag = True
        temp.append(word)
    shortcut[word[0].lower()] = " ".join(temp)

    if not flag:
        for t in tmp:
            if t.isalpha():
                if t.lower() not in shortcut:
                    shortcut[t.lower()] = tmp[:tmp.index(t)] + "[" + t + "]" + tmp[tmp.index(t) + 1:]
                    mapping[i] = t.lower()
                    break

for i in range(N):
    if i not in mapping:
        print(data[i])
    else:
        print(shortcut[mapping[i]])

print(shortcut)