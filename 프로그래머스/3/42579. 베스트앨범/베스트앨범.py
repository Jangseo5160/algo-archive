def solution(genres, plays):
    answer = []
    summary_dict = {}
    # {{'gen': 'pop', 'total': 170, 'list': [(-2500,2), (-2500,4)]},
    # {'gen': 'pop', 'total': 170, 'list': [(-2500,2), (-2500,4)]},}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in summary_dict:
            summary_dict[genre]= {
                'total': 0, 
                'list': []
            }
        summary_dict[genre]['total']+=play
        summary_dict[genre]['list'].append((-play, idx))
    
    summary_dict = sorted(summary_dict.items(), key = lambda x: x[1]['total'], reverse=True)
    for gen, info in summary_dict:
        info['list'].sort(key=lambda x: x[0])
    
    for gen, info in summary_dict:
        answer.append(info['list'][0][1])
        if len(info['list'])>1:
            answer.append(info['list'][1][1])
        
    return answer