
import heapq

INF = int(1e9)

start = 0

m,n = list(map(int,input().split(" ")))

array=[]

for _ in range(m):
    array.append(list(map(str, input().split(" "))))


graph = [[] for i in range(n*m)]

distance = [INF] * (n*m)

for i in range(m):  #노드의 생성과정 4*4의 경우 16개의 노드 생성
    for j in range(n):
        if j+1<m:
            if array[i][j]=='R': # R이라면 오른쪽 노드로의 간선 값 은 0
                graph[i * m + j].append((i * m + j + 1, 0))
            else :   # R이 아니라면 간선 값은 1
                graph[i * m + j].append((i * m + j + 1, 1))
        if j-1>=0:
            if array[i][j]=='L':
                graph[i * m + j].append((i * m + j - 1, 0))
            else :
                graph[i * m + j].append((i * m + j - 1, 1))
        if i-1>=0:
            if array[i][j]=='U':
                graph[i * m + j].append(((i-1) * m + j, 0))
            else :
                graph[i * m + j].append(((i-1) * m + j, 1))
        if i+1<n:
            if array[i][j]=='D':
                graph[i * m + j].append(((i+1) * m + j, 0))
            else :
                graph[i * m + j].append(((i+1) * m + j, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[len(distance)-1])