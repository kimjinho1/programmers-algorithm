from collections import defaultdict

def solution(id_list, report, k):
    report_user_dict = defaultdict(set)
    report_cnt_dict = defaultdict(int)
    ans = []
    
    for arg in set(report):
        id, reported_id = arg.split()
        report_user_dict[id].add(reported_id)
        report_cnt_dict[reported_id] += 1
        
    for id in id_list:
        cnt = 0
        for reported_id in report_user_dict[id]:
            if report_cnt_dict[reported_id] >= k:
                cnt += 1 
        ans.append(cnt)

    return ans