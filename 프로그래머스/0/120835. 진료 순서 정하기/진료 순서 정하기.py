def solution(emergency):
    answer = []
    idx = []
    idx = sorted(emergency,reverse=True)
    for i in range(len(idx)):
        answer.append(idx.index(emergency[i])+1)
    print(idx)
    return answer