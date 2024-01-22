def solution(array, height):
    answer = 0
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)