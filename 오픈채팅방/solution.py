def solution(records):
    user_dic = {}
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    ans = []
    
    for record in records:
        li = record.split()
        if li[0] in ["Enter", "Change"]:
            user_dic[li[1]] = li[2]

    for record in records:
        li = record.split()
        if li[0] != "Change":
            ans.append(user_dic[li[1]] + printer[li[0]])
            
    return ans