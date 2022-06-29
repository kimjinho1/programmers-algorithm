from collections import deque

def solution(N, edge):
    graph = [[] for _ in range(N+1)]
    q = deque([1])
    check_li = [-1]*(N+1)
    check_li[1] = 0
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check_li[n] == -1:
                q.append(n)
                check_li[n] = check_li[node] + 1
    
    return check_li.count(max(check_li))