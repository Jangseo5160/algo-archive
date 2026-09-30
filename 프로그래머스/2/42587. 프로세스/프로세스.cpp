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
        int cur = q.front();
        q.pop();
        if(priorities[cur] ==max_v){
            answer++;
            if(cur == location) return answer;
            priorities[cur] = -1;
            max_v=*max_element(priorities.begin(), priorities.end());
        }
        else if(priorities[cur]<max_v){
            q.push(cur);
        }
    }
    
    
    
    return answer;
}