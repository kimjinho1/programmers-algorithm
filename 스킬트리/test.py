from solution import solution

test_list = [["CBD", ["BACDE", "CBADF", "AECB", "BDA"]]]
test_result = [solution(*input) for input in test_list]
ans = [2]

print(test_result)
print(test_result == ans)