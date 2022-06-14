from solution import solution

test_list = [["one4seveneight"], ["23four5six7"], 	["2three45sixseven"], ["123"]]
test_result = [solution(*input) for input in test_list]
ans = [1478, 234567, 234567, 123]

print(test_result)
print()
print(test_result == ans)