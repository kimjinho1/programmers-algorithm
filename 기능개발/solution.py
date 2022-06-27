from math import ceil
from collections import deque

def solution(progresses, speeds):
    ans = []
    q = deque([ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))])
    max_t = 0
    while q:
        t = q.popleft()
        if not ans or t > max_t:
            max_t = t
            ans.append(1)
        else:
            ans[-1] += 1

    return ans