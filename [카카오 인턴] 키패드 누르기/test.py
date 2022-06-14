from lib2to3.pgen2.literals import test
from solution import solution

test_list = [[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"], [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]]
test_result = [solution(*input) for input in test_list]
ans = ["LRLLLRLLRRL", "LRLLRRLLLRR", "LLRLLRLLRL"]

print(test_result)
print()
print(test_result == ans)