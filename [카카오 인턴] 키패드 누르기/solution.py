def get_idx(n):
    n = 10 if n == 0 else n-1
    
    return [n//3, n%3]

def get_distance(n1, n2):
    d1, d2 = get_idx(n1), get_idx(n2)
    d = abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])

    return d
    
def get_nexthand(left, right, num, hand):
    if num in [1, 4, 7]:
        return 'left'
    elif num in [3, 6, 9]:
        return 'right'
    else:
        dl = get_distance(left, num)
        dr = get_distance(right, num)
        if dl < dr:
            return 'left'
        elif dl > dr:
            return 'right'
        elif dl == dr:
            return hand
    
def solution(numbers, hand):    
    left, right = 10, 12
    ans = ''
    
    for num in numbers:
        nexthand = get_nexthand(left, right, num, hand)
        if nexthand == "left":
            left = num
            ans += 'L'
        else:
            right = num
            ans += 'R'
    
    return ans