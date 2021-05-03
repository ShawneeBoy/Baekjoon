# 2021.05.03
# Attempts: 1

from collections import deque


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfsResult = []
bfsResult = []
for nodeList in graph:
    nodeList.sort()


def dfs(v):
    if(visited[v] == 1):
        return False
    else:
        visited[v] = 1
        dfsResult.append(v)
        for node in graph[v]:
            dfs(node)
        return True


bfsQueue = deque()


def bfs(v):
    visited[v] = 1
    bfsResult.append(v)
    for node in graph[v]:
        bfsQueue.append(node)
    while(len(bfsQueue) != 0):
        currNode = bfsQueue.popleft()
        if(visited[currNode] == 1):
            continue
        else:
            visited[currNode] = 1
            bfsResult.append(currNode)
            for i in graph[currNode]:
                bfsQueue.append(i)


dfs(v)
visited = [0] * (n+1)
bfs(v)


for i in range(len(dfsResult)-1):
    print(dfsResult[i], end=" ")
print(dfsResult[-1])

for i in range(len(bfsResult)-1):
    print(bfsResult[i], end=" ")
print(bfsResult[-1])
