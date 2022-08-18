INF = int(1e9) #무한
n,m = map(int,input().split()) #노드 갯수

graph = [[INF] * (n + 1) for _ in range(n + 1)] #2차원 배열 무한대로 초기화

# 자기자신 -> 자기자신 // 0으로 초기화 (대각선)
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보로 초기화
for _ in range(m):
    a, b = map(int, input().split()) # a-> b 비용 1
    graph[a][b] = 1
    graph[b][a]=1 #양방향 이동 가능

x,k = map(int,input().split())


# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1): #노드 갯수
    for a in range(1, n + 1): #a (출발)
        for b in range(1, n + 1): #b (도착)
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) #a->b vs a->k->b

# 수행된 결과 출력
if graph[1][k]==1e9 or graph[k][x]==1e9:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])

graph[1][k]+graph[k][x]
