from solution import solution

test_list = [[[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"], ["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]]]
test_result = [solution(*input) for input in test_list]
ans = [[1, 0, 1, 1, 1, 0]]

print(test_result)
print()
print(test_result == ans)