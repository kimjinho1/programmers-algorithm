from solution import solution

test_list = [[[93, 30, 55], [1, 30, 5]], [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]]]
test_result = [solution(*input) for input in test_list]
ans = [[2, 1], [1, 3, 2]]

print(test_result)
print(test_result == ans)