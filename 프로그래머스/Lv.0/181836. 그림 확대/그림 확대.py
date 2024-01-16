def solution(picture, k):
    answer = []
    temp = []
    for i in picture:
        for j in range(len(i)):
            for _ in range(k):
                answer.append(i[j])
        for _ in range(k):
            temp.append(''.join(answer))
        
        answer.clear()
    
    return temp