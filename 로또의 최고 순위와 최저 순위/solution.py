def solution(lottos, win_nums):
    t = lottos.count(0)
    cnt = len([n for n in lottos if n in win_nums])
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    return rank[t+cnt], rank[cnt]