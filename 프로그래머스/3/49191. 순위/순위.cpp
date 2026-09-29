#include <string>
#include <vector>
#include <queue>
using namespace std;

void dfs(int cur, vector<vector<int>>& graph, vector<bool>& visited){
    visited[cur] = true;
        
    for(auto next: graph[cur]){
        if(!visited[next]){
            dfs(next, graph, visited);
        }
    }
}

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector<int>> win(n+1);
    vector<vector<int>> loose(n+1);

    for(auto a:results){
        win[a[0]].push_back(a[1]);
        loose[a[1]].push_back(a[0]);
    }


    for(int i=1; i<=n; i++){
        vector<bool> w_visited(n+1, false);
        vector<bool> l_visited(n+1, false);
        dfs(i, win, w_visited);
        dfs(i, loose, l_visited);
        int cnt=0;
        for(int j=1; j<=n; j++){
            if(i!=j){
                if(w_visited[j] || l_visited[j]) cnt++;
            }
        }
        if(cnt==n-1) answer++;
    }

    return answer;
}









//     queue<int> wq;
//     queue<int> lq;
    
//     for(int i=1; i<=n; i++){
//         if(loose[i].size()+win[i].size()==n-1){
//             answer++;
            
//             }
            
//             lq.push(loose[i]);
//             while(!wq.empty()){
//                 wq.top();
//             }
//         }
//     }