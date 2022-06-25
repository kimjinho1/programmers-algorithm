def solution(dartResult):
    dart = {'S': 1, 'D': 2, 'T': 3}
    n = ''
    score = []

    for c in dartResult:
        if c.isnumeric():
            n += c
        elif c in dart:
            score.append(int(n) ** dart[c])
            n = ''
        elif c == '*':
            score[-2:] = [s*2 for s in score[-2:]]
        elif c == '#':
            score[-1] = -score[-1]       

    return sum(score)