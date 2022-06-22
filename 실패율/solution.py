from collections import Counter

def solution(N, stages):
    ans = []
    n = len(stages)
    counter = Counter(stages)
    for i in range(1, N+1):
        if n:
            ans.append(counter[i] / n)
            n -= counter[i]
        else:
            ans.append(0)
                
    return [i+1 for i in sorted(range(N), key=lambda x : ans[x], reverse=True)]