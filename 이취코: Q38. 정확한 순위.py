import sys
input= sys.stdin.readline
INF = int(1e9) #무한
n,m = map(int,input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)] #2차원 배열 무한대로 초기화

# 자기자신 -> 자기자신 // 0으로 초기화 (대각선)
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보로 초기화
for _ in range(m):
    a, b= map(int, input().split()) # a-> b
    graph[a][b]= 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1): #노드 갯수
    for a in range(1, n + 1): #a (출발)
        for b in range(1, n + 1): #b (도착)
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) #a->b vs a->k->b

# 수행된 결과 출력
h=0
for a in range(1, n + 1):
    cont=0
    for b in range(1, n + 1):
        if graph[a][b] != 1e9 or graph[b][a] != 1e9: #a->b나 b->a가 있을경우
            cont+=1
    if cont==n: #들어오는 노드+나가는 노드 = 전체 사람수 -1(자신) ==> 모든 노드랑 연결되어 있어 순위를 알수 있다
        h+=1

print(h)
