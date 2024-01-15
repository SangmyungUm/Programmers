def solution(arr):
    answer = []
    i = 0
    if len(arr) == 1:
        return arr
    while True:
        if len(arr)>=2**i and len(arr)<=2**(i+1):
            break;
        else: i+=1
    for i in range(2**(i+1)-len(arr)):
        arr.append(0)
    
    return arr