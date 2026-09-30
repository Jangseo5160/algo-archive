#include <string>
#include <vector>
#include<queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    queue<pair<int, int>> q;
    int now=0;
    int sum=0;
    int i=0;
    
    while(i<truck_weights.size() || !q.empty()){
        now++;
        if(!q.empty() && now-q.front().second == bridge_length){
            sum-=q.front().first;
            q.pop();
        }
        if(i<truck_weights.size() && sum+truck_weights[i]<=weight){
            q.push({truck_weights[i], now});
            sum+=truck_weights[i];
            i++;
        }
    }
    
    return now;
    
}