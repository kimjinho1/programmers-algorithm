def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        b = bin(arr1[i] | arr2[i])[2:]
        ans.append((n - len(b))*' ' + b.replace('1', '#').replace('0', ' '))
        
    return ans