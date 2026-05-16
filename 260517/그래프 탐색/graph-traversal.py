import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited=[False]*(n+1)
count=0

# Please write your code here.
graph=[[] for _ in range(n+1)]

for x,y in edges:
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    visited[node]=True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(sum(visited)-1)