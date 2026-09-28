#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<vector<int>> graph(n+1);
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(computers[i][j]==1)
                graph[i].push_back(j);
        }
    }
    
    queue<int> q;
    vector<bool> v(n, false);
    
    for(int i=0; i<n; i++){
        if(q.empty()){
            if(!v[i]){
                q.push(i);
                answer++;
            }
        }
        while(!q.empty()){
            int cur = q.front();
            q.pop();
            
            for(auto a: graph[cur]){
                if(!v[a]) {
                    q.push(a);
                    v[a]=true;
                }
            }
        }
    
    }
    return answer;
}