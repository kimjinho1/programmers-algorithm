from solution import solution

test_list = [["1S2D*3T"], ["1D2S#10S"], ["1D2S0T"], ["1S*2T*3S"], ["1D#2S*3S"], ["1T2D3D#"], ["1D2S3T*"]]
test_result = [solution(*input) for input in test_list]
ans = [37, 9, 3, 23, 5, -4, 59]

print(test_result)
print()
print(test_result == ans)