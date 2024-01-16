def solution(arr):
    answer = 0
    Arr=[]
    j = 0
    
    while True:      
        Arr= arr[:]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 ==0:
                arr[i] = arr[i]//2
            elif arr[i] < 50 and arr[i] % 2 ==1:
                arr[i] = arr[i]*2+1       
        print(answer)

        if Arr == arr[:]:           
            return answer       
        else:
            Arr != arr
            Arr=arr[:]
        
        answer+=1
                
            
    return answer