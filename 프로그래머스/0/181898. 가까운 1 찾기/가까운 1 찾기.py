def solution(arr, idx):
    answer = 0
    while idx < len(arr):
        if arr[idx]: return idx
        idx+=1
    return -1