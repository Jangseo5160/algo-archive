#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    vector<vector<int>> graph(n+1);
    for(auto a:wires){
        graph[a[0]].push_back(a[1]);
        graph[a[1]].push_back(a[0]);
    }
    for(auto a: wires){
        int cut_a=a[0];
        int cut_b=a[1];
        vector<bool> visited(n+1, false);
        queue<int> q;
        
        q.push(1);
        visited[1]=true;
        
        int cnt=0;
        

        while (!q.empty()){
            auto cur = q.front();
            q.pop();
            cnt++;
            
            for(auto next: graph[cur]){
                if((cur==cut_a && next==cut_b)|| cur==cut_b && next==cut_a){
                    continue;
                }
                if(!visited[next]){ 
                    q.push(next);
                    visited[next]=true;
                }
            }
        }
        int other = n-cnt;
        answer= min(answer, abs(cnt-other));
    }
    
    return answer;
}