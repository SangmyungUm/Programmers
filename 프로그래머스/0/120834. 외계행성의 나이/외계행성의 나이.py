def solution(age):
    answer = ''
    p962 = ["a","b","c","d",'e','f','g','h','i','j']
    temp = str(age)
    for i in range(len(temp)):
        answer += p962[int(temp[i])]
    return answer