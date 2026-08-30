def solution(cacheSize, cities):
    answer = 0
    if cacheSize ==0:
        return len(cities) * 5
    
    
    can = [0] * cacheSize
    miss = 0
    hit = 0
    for city in cities:
        city = city.lower()
        
        if city not in can:
            miss+=1
            if can:
                del can[0]
            can.append(city)
        else:
            can.remove(city)
            can.append(city)
            hit+=1
            
    answer = miss*5 + hit
    return answer