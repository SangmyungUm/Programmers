def solution(arr):
    stk = []
    i = 0

    for i in range(len(arr)):
        if stk == []:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()

        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            

    if stk == []:
        stk.append(-1)
            
    return stk