def solution(sequence):
    answer = 0
    def kadane(sequence):
        max_sum = sequence[0]
        current = sequence[0]
        for x in sequence[1:]:
            current = max(x, current+x)
            max_sum = max(max_sum, current)
        return max_sum
    
    q1 = [sequence[i] * (1 if i%2==0 else -1) for i in range(len(sequence))]
    q2 = [sequence[i] * (-1 if i%2==0 else 1) for i in range(len(sequence))]
    
    
    return max(kadane(q1), kadane(q2))