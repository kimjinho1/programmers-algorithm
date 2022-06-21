from solution import solution

test_list = [[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]], [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]], [["XYZ", "XWY", "WXA"], [2,3,4]]]
test_result = [solution(*input) for input in test_list]
ans = [["AC", "ACDE", "BCFG", "CDE"], ["ACD", "AD", "ADE", "CD", "XYZ"], ["WX", "XY"]]

print(test_result)
print()
print(test_result == ans)