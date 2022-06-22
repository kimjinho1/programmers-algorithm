import sys
from collections import deque
sys.setrecursionlimit(10000)

def solution(places):    
    def bfs(i, j):
        q = deque([(i, j)])
        while q:
            y, x = q.popleft()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                Y, X = y+dy, x+dx
                d = abs(Y-i) + abs(X-j)
                if d <= 2 and (0 <= Y < 5) and (0 <= X < 5) and check_li[Y][X] == 0:
                    check_li[Y][X] = 1
                    if place[Y][X] == 'P':
                        return 0
                    elif place[Y][X] == 'O':
                        q.append((Y, X))
        return 1
    
    ans = []
    for place in places:
        check_li = [[0]*5 for _ in range(5)]
        check = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and check_li[i][j] == 0:
                    check_li[i][j] = 1
                    check = check and bfs(i, j)
        ans.append(check)                    
                    
    return ans