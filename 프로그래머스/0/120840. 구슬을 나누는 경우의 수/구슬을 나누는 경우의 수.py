def solution(balls, share):
    answer = 0
    N=1
    NM=1
    for i in range(balls,share,-1):
        N *= i
    for i in range(1,balls-share+1):
        NM *= i
    print(N,NM)
    return N/NM