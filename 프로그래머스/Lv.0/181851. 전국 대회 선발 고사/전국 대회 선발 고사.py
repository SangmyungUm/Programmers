def solution(rank, attendance):
    answer = 0
    temp= []
    for i in range(len(rank)):
        if attendance[i] == True:
            temp.append(rank[i])
    
    temp.sort()
    a, b, c = temp[0], temp[1], temp[2]
    
    print(temp,a,b,c)
    answer = rank.index(a)*10000+rank.index(b)*100+rank.index(c)
    return answer 