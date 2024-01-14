def solution(num_list):
    answer = 0
    list1 = list(num_list)
    odd = ""
    even = ""
    for i in range(len(list1)):
        if list1[i]%2 == 0:
            even += str(list1[i])
        else:
            odd += str(list1[i])
        
    answer = int(odd)+int(even)
            
    return answer