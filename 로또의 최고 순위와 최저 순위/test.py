from solution import solution

test_list = [[[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]], 
            [[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]], 
            [[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]]]
test_result = [list(solution(*input)) for input in test_list]
ans = [[3, 5], [1, 6], [1, 1]]

print(test_result)
print()
print(test_result == ans)