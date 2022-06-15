def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    matching_num_cnt = sum([n in win_nums for n in lottos])
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    return rank[zero_cnt+matching_num_cnt], rank[matching_num_cnt]