def solution(arr, queries):
    answer = []
    templist=[]
    for s, e, k in queries:
        temp =[i for i in arr[s:e+1]] 
        
        for i in range(len(temp)):
            if temp[i]>k:
                templist.append(temp[i])
        
        if templist == []:
            answer.append(-1)
        else:
            answer.append(min(templist))
        templist.clear()
            
                
            
                
        
        
            
            
        
        
                
    return answer