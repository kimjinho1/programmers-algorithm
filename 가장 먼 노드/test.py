from solution import solution

test_list = [[6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]]]
test_result = [solution(*input) for input in test_list]
ans = [3]

print(test_result)
print(test_result == ans)