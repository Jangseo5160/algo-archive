#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
vector<string> answer;
vector<bool> visited;
bool found; 

void dfs(string curr, vector<vector<string>>& tickets, vector<string>& path){
    if(found) return;
    if(path.size() == tickets.size()+1){
        answer=path;
        found = true;
        return;
    }
    for(int i=0; i<tickets.size(); i++){
        if(!visited[i]&&tickets[i][0]==curr){
            visited[i]=true;
            path.push_back(tickets[i][1]);
            dfs(tickets[i][1], tickets, path);
            path.pop_back();
            visited[i]=false;
        }
    }
}


vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    visited.assign(tickets.size(), false);
    vector<string> path;
    path.push_back("ICN");
    dfs("ICN",tickets, path);
    
    return answer;
}