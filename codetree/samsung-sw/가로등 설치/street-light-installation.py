import sys
import heapq
import bisect
import math

##############################################

input = sys.stdin.readline
Q = int(input())
line = list(map(int, input().split()))
N, M = line[1], line[2]
lights = line[3:]

##############################################
id_to_pos  = {}
pos_to_id  = {}
pos_list   = []
max_heap   = []
removed    = set()
next_id    = M+1
result     = []
#################################################
# 가로등 등록
for i, pos in enumerate(lights):
    id_to_pos[i+1] = pos # 삭제할 때 
    bisect.insort(pos_list, pos) 

# heap 설정
for i in range(len(pos_list)-1):
    left = pos_list[i]
    right = pos_list[i+1]
    dist = right-left
    heapq.heappush(max_heap, (-dist, left))

#################################################
def add_light():
    global next_id

    while max_heap:
        neg_dist, left_pos = heapq.heappop(max_heap)
        dist = -neg_dist

        idx = bisect.bisect_left(pos_list, left_pos)
        if idx >= len(pos_list) or pos_list[idx] != left_pos:
            continue
        if idx+1 >= len(pos_list) or pos_list[idx+1]!= left_pos+dist:
            continue
        break
    
    new_pos = math.ceil((left_pos + left_pos + dist)/2)
    bisect.insort(pos_list, new_pos)
    id_to_pos[next_id] = new_pos
    next_id +=1

    heapq.heappush(max_heap, (-(new_pos - left_pos), left_pos))
    heapq.heappush(max_heap, (-(left_pos + dist - new_pos), new_pos))

#################################################
def remove_light(D):
    del_pos = id_to_pos[D]
    idx = bisect.bisect_left(pos_list, del_pos)
    pos_list.pop(idx)
    del id_to_pos[D]

    left_pos = pos_list[idx-1]  if idx-1>=0             else None
    right_pos = pos_list[idx]   if idx < len(pos_list)  else None
    if left_pos is not None and right_pos is not None:
        dist = right_pos - left_pos 
        heapq.heappush(max_heap, (-dist, left_pos))

#################################################
def cal_max_gap():
    max_gap=0
    left_gap = (pos_list[0]-1)*2
    right_gap = (N-pos_list[-1])*2

    while max_heap:
        neg_dist, left_pos = max_heap[0]
        dist = -neg_dist

        idx = bisect.bisect_left(pos_list, left_pos)
        if idx >=len(pos_list) or pos_list[idx] != left_pos:
            heapq.heappop(max_heap)
            continue
        if idx+1 >=len(pos_list) or pos_list[idx+1] != left_pos+dist:
            heapq.heappop(max_heap)
            continue
        break
    max_gap = -max_heap[0][0] if max_heap else 0
    max_gap = max(left_gap, right_gap, max_gap)
    print(max_gap)
    
#################################################
for _ in range(Q):
    cmd = list(map(int, input().split()))
    if not cmd:
        continue
    if cmd[0] == 200:
        add_light()

    if cmd[0] == 300:
        D = cmd[1]
        remove_light(D)

    if cmd[0] == 400:
        cal_max_gap()

print('\n'.join(map(str, result)))

