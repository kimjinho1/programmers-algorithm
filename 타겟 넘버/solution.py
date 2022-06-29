def dfs(n, numbers, target, i):
    if i == len(numbers):
        return 1 if n == target else 0
    return dfs(n + numbers[i], numbers, target, i+1) + dfs(n - numbers[i], numbers, target, i+1)

def solution(numbers, target):
    return dfs(0, numbers, target, 0)