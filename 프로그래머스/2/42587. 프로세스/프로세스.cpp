#include <string>
#include <vector>
#include<algorithm>
#include<queue>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int max_v=*max_element(priorities.begin(), priorities.end());
    queue<int> q;
    int cnt=0;
    
    for(int i=0; i<priorities.size(); i++){
        q.push(i);
    }
    
    while(!q.empty()){
        int cur_idx = q.front();
        q.pop();
        if(priorities[cur_idx] == max_v){
            cnt++;
            if(cur_idx==location) return cnt;
            priorities[cur_idx] = -1;
            max_v=*max_element(priorities.begin(), priorities.end());
        }
        else{
            q.push(cur_idx);
        }
    }
    return answer;
}