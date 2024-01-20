def solution(numbers):
    answer = -1e9
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j: continue
            if numbers[i] *numbers[j] >=answer:
                answer = numbers[i] *numbers[j]
    return answer