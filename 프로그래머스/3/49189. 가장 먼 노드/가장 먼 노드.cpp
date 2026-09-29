#include <string>
#include <vector>
#include<queue>
#include<algorithm>
#include<iostream>
using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    vector<vector<int>> graph(n+2);
    vector<int> dist(n+2,-1);
    for(auto e:edge){
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }
    queue<int> q;
    q.push(1);
    dist[1]=0;
    while(!q.empty()){
        int cur=q.front();
        q.pop();
        for(auto next:graph[cur]){
            int next_dist=dist[cur]+1;
            if(dist[next]==-1){
                dist[next]=next_dist;
                q.push(next);
            }
        }
    }

    int max_v=*max_element(dist.begin(), dist.end());
    for(auto d: dist){
        if(d==max_v) answer++;
    }
    
    return answer;
}