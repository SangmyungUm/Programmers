def solution(myString):

    
    answer=list(myString.split('x'))
    answer = ' '.join(answer).split()
    answer.sort()
    
    return answer