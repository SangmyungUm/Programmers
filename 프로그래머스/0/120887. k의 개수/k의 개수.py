def solution(i, j, k):
    answer = 0
    for x in range(i,j+1):
        temp = str(x).count(str(k))
        answer += temp
    return answer