def solution(n):
    answer = 2
    i = 0
    while True:
        if n==i**2:
            answer = 1
            break;
        if i == n:
            break;
        i+=1
    return answer