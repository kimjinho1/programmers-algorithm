import sys
sys.setrecursionlimit(10000)

def solution(places):    
    def bfs(i, j):
        q = [(i, j)]
        while q:
            y, x = q.pop(0)
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                Y, X = y+dy, x+dx
                if 0 <= Y < 5 and 0 <= X < 5 and abs(Y-i) + abs(X-j) <= 2:
                    if place[Y][X] == 'O':
                        place[Y][X] = 'X'
                        q.append((Y, X))
                    elif place[Y][X] == 'P':
                        return 0
        return 1
    
    ans = []
    for place in places:
        place = list(map(list, place))
        check = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    place[i][j] = 'X'
                    check &= bfs(i, j)
        ans.append(check)                       
                    
    return ans