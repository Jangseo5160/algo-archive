#include <string>
#include <vector>

using namespace std;
vector<bool> visited;
int answer = 0;

void dfs(int k,vector<vector<int>> dungeons, int cnt){
    answer = max(answer, cnt);
    
    for(int i=0; i<dungeons.size(); i++){
        if(!visited[i] && dungeons[i][0]<=k){
            visited[i]=true;
            dfs(k-dungeons[i][1], dungeons, cnt+1);
            visited[i]=false;
        }
    }
    
}


int solution(int k, vector<vector<int>> dungeons) {
    visited.assign(dungeons.size(), false);
    dfs(k, dungeons, 0);
    return answer;
}