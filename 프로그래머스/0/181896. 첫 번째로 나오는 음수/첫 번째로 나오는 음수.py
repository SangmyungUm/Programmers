def solution(num_list):
    answer = 0
    list1 = list(num_list)
    for i in range(len(list1)):
        if list1[i] >= 0:
            answer = -1
        else: 
            answer = i
            break
    return answer