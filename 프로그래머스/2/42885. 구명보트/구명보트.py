def solution(people, limit):
    people.sort()
    light=0
    heavy=len(people)-1
    boat=0
    
    while light<=heavy:
        if people[light]+people[heavy]<=limit:
            light+=1
        heavy-=1
        boat+=1
        
        
    return boat