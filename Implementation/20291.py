import sys
input = sys.stdin.readline

N = int(input().strip())

extension = {}

for _ in range(N):
    file_name, extension_ = input().strip().split(".")
    if extension_ not in extension:
        extension[extension_] = 1
    else:
        extension[extension_] += 1

answer = sorted(extension.items())

for a,r in answer:
    print(a,r)