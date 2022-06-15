from solution import solution

test_list = [[["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]]]
test_result = [solution(*input) for input in test_list]
ans = [["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]]

print(test_result)
print()
print(test_result == ans)