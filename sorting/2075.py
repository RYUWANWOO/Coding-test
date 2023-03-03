import sys
import heapq

heap = []
n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if len(heap) < n:
            heapq.heappush(heap,data[i][j])
        else:
            if heap[0] < data[i][j]:
                heapq.heappop(heap)
                heapq.heappush(heap,data[i][j])


print(heap[0])
