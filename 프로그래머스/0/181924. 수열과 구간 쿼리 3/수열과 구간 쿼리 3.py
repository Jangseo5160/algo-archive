def solution(arr, queries):
    answer = []
    for a, b in queries:
        arr[a], arr[b] = arr[b], arr[a] 
        # 튜플 생성 => 내부적으로 (arr[a], arr[b]) 튜플이 생성됨
    return arr