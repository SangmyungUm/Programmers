from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []
    a=[numer1,denom1]
    b=[numer2,denom2]
    if a[1] != b[1]:
        a[0] =a[0]*b[1]        
        b[0] =b[0]*a[1]
        a[1] =a[1]*b[1]
        b[1] =a[1]
        answer = [a[0] + b[0],a[1] ]
        print(answer)
    else:
        answer=[numer1+numer2,denom1]
    # while True:
    #     if answer[0]%i==0 and answer[1]%i==0:
    #         answer[0]= answer[0]/i
    #         answer[1]= answer[1]/i
    #         break
    #     i -=1
    for i in range(min(answer),0,-1):
        if answer[0]%i==0 and answer[1]%i==0:
            answer[0]= answer[0]/i
            answer[1]= answer[1]/i
            break
            
    return answer