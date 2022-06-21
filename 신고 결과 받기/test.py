from solution import solution

test_list = [[["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2], [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3]]
test_result = [solution(*input) for input in test_list]
ans = [[2,1,1,0], [0, 0]]

print(test_result)
print()
print(test_result == ans)