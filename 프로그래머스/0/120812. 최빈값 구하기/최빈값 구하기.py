def solution(array):
    # answer = 0
    # a =list(set(array))
    # cnt = []
    # print(a)
    # for i in a:
    #     cnt.append(array.count(i))
    # # answer = a.index(max(cnt))
    # if cnt.count(max(cnt)) >1:
    #     return -1
    # return max(cnt)
    a= list(set(array))
    print(a)
    cnt = []
    for i in a:
        cnt.append(array.count(i))
        
    print(cnt)
    print(a[cnt.index(max(cnt))])
    if cnt.count(max(cnt)) >1:
        return -1

    return a[cnt.index(max(cnt))]