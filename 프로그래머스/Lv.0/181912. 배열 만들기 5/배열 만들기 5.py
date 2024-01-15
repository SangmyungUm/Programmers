def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        print(i[s:s+l])
        if int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
#         if int(i[s:l]) > k:
#             answer.append(i[s:l])
        
    return answer