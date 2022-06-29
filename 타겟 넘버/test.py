from solution import solution

test_list = [[[1, 1, 1, 1, 1], 3], [[4, 1, 2, 1], 4]]
test_result = [solution(*input) for input in test_list]
ans = [5, 2]

print(test_result)
print(test_result == ans)