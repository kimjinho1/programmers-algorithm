def solution(new_id):
    ans = ""

    # 1
    new_id = new_id.lower()
    
    # 2
    for c in new_id: 
        if c.isalnum() or c in "-_.":
            ans += c
    
    # 3
    while ".." in ans:
        ans = ans.replace("..", '.')
    
    # 4
    if ans and ans[0] == '.':
        ans = ans[1:]
    if ans and ans[-1] == '.':
        ans = ans[:-1]
    
    # 5
    if ans == '':
        ans = 'a'
    
    # 6
    if len(ans) >= 16:
        ans = ans[:15]
        if ans[-1] == '.':
            ans = ans[:-1]
    
    # 7
    while len(ans) < 3:
        ans += ans[-1]
        
    return ans