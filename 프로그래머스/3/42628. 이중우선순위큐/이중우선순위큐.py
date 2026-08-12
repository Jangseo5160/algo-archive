import heapq

def solution(operations):
    answer = []
    for i in operations:
        if i.startswith("I"):
            num = int(i.split()[1])
            heapq.heappush(answer, num)
            
        elif i == "D -1":
            if answer:
                heapq.heappop(answer)
                
        elif i == "D 1":
            if answer:
                neg_ans = []
                
                for num in answer:
                    heapq.heappush(neg_ans, -num)
                heapq.heappop(neg_ans)
                
                answer= []
                
                for num in neg_ans:
                    heapq.heappush(answer, -num)
    if not answer:
        return [0,0]
    min_num = answer[0]
    max_num = max(answer)
    return [max_num, min_num]
