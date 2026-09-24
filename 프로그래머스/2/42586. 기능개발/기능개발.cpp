#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector <int> days;
    queue<int> q;
    for(auto i=0; i<progresses.size(); i++){
        days.push_back((100-progresses[i]+speeds[i]-1)/speeds[i]);
    }
    
    for(auto a: days){
        if(q.empty() || q.front()>=a){
            //동일할때
            q.push(a);
        } 
        else{
            int cnt=0;
            while(!q.empty()){
                q.pop();
                cnt++;
            }
            answer.push_back(cnt);
            q.push(a);
        }
    }
    if(!q.empty()){
        answer.push_back(q.size());
    }
    

    return answer;
}