def solution(genres, plays):
    answer = []
    hash_map = {}
    song_list = {}
    
    for idx, gen in enumerate(genres):
        if gen not in hash_map:
            hash_map[gen]= 0
            song_list[gen] = []
        hash_map[gen]+=plays[idx]
        song_list[gen].append([plays[idx], idx])
        
    hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

    for gen in song_list:
        song_list[gen].sort(key = lambda x: (x[0], -x[1]))
        
    for genre, total in hash_map:
        play, idx = song_list[genre].pop()
        answer.append(idx)
        if len(song_list[genre])>0:
            play, idx = song_list[genre].pop()
            answer.append(idx)
    return answer