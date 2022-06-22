from solution import solution

test_list = [[5, [2, 1, 2, 6, 2, 4, 3, 3]], [4, [4,4,4,4,4]]]
test_result = [solution(*input) for input in test_list]
ans = [[3,4,2,1,5], [4,1,2,3]]

print(test_result)
print()
print(test_result == ans)