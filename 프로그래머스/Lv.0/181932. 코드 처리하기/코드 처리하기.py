def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0 and i%2 == 0 and code[i]!='1':
            answer += code[i]
        elif mode == 1 and i%2 == 1 and code[i]!='1':
            answer += code[i]
        elif code[i] == '1' :
            mode = not mode 
    if answer == '':
        answer = "EMPTY"
        
            
            
        
        
    return answer





# def solution(code):
#     answer = ''
#     mode=0
#     for idx in range(len(code)):
#         if code[idx] != 1 and idx%2==0 and mode ==0:
#             answer+=code[idx]
#         elif code[idx] != 1 and idx%2==1 and mode == 1:
#             answer += code[idx]
#         elif code[idx] == 1 and mode ==0:
#             mode =1
#         elif code[idx] == 1 and mode ==1:
#             mode =0
        
        
#     return answer