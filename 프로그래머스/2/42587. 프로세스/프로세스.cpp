#include <string>
#include <vector>
#include<queue>
#include<iostream>
#include<algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int max_v = *max_element(priorities.begin(), priorities.end());
    queue<int> q;
    for(int i=0; i<priorities.size(); i++){
        q.push(i);
    }
    
    while(!q.empty()){
        if(priorities[q.front()] ==max_v){
            answer++;
            if(q.front() == location) return answer;
            priorities[q.front()] = -1;
            q.pop();
            max_v=*max_element(priorities.begin(), priorities.end());
        }
        else if(priorities[q.front()]<max_v){
            int temp = q.front();
            q.pop();
            q.push(temp);
        }
    }
    
    
    
    return answer;
}