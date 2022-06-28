from collections import deque

def solution(skill, skill_trees):
    ans = 0
    for skill_tree in skill_trees:
        q = deque(skill)
        for s in skill_tree:
            if s in q and s != q.popleft():
                break
        else:
            ans += 1
        
    return ans