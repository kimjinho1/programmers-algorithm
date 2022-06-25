def binary(num, n):
    b = bin(num)[2:]
    return (n - len(b))*'0' + b

def str_sum(n, s1, s2):
    s = ''
    for i in range(n):
        s += '#' if s1[i] == '1' or s2[i] == '1' else ' '
    return s

def solution(n, arr1, arr2):
    ans = [0] * n
    for i in range(n):
        ans[i] = str_sum(n, binary(arr1[i], n), binary(arr2[i], n))
    return ans