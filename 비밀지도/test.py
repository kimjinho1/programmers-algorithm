from solution import solution

test_list = [[	5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]], [	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]]]
test_result = [solution(*input) for input in test_list]
ans = [["#####", "# # #", "### #", "#  ##", "#####"], ["######", "###  #", "##  ##", " #### ", " #####", "### # "]]

print(test_result)
print()
print(test_result == ans)