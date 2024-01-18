def solution(n, k):
    answer = 0
    if n>=10:
        answer = n//10
    return n*12000+k*2000-answer*2000