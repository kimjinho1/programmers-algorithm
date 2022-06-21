from collections import Counter
from itertools import combinations

def solution(orders, course):   
    ans = []
    for n in course:
        comb_li = []
        for order in orders:
            comb_li.extend(list(combinations(sorted(order), n)))

        counter = Counter(comb_li)
        if counter and max(counter.values()) > 1:
            ans.extend([''.join(k) for k in counter if counter[k] == max(counter.values())])

    return sorted(ans)