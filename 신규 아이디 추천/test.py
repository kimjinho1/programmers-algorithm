from solution import solution

test_list = [["...!@BaT#*..y.abcdefghijklm"], ["z-+.^."], ["=.="], ["123_.def"], ["abcdefghijklmn.p"]]
test_result = [solution(*input) for input in test_list]
ans = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]

print(test_result)
print()
print(test_result == ans)