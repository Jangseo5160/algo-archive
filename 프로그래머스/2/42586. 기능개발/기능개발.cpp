#include <string>
#include <vector>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> avail;
    queue<int> q;
    for(int i=0; i<progresses.size(); i++){
        avail.push_back(((100-progresses[i])+speeds[i]-1)/speeds[i]);
    }
    for(auto a:avail){
        if(q.empty()) q.push(a);
        else{
            if(q.front()>=a){
                q.push(a);
            }
            else{
                int cnt=0;
                while(!q.empty()){
                    q.pop();
                    cnt++;
                }
                q.push(a);
                answer.push_back(cnt);
            }
        }
    }
    
    int cnt=0;
    while(!q.empty()){
        q.pop();
        cnt++;
    }
    answer.push_back(cnt);
    
    
    return answer;
}