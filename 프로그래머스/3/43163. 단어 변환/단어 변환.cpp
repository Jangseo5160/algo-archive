#include <string>
#include <vector>
#include<queue>
#include<unordered_map>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    unordered_map<string, int> visited;
    queue<string> q;
    q.push(begin);
    visited[begin]=0;
    
    while(!q.empty()){
        string cur = q.front();
        q.pop();
        
        for(auto w:words){
            if(!visited.contains(w)){
                int cnt=0;
                for(int i=0; i<w.size(); i++){
                    if(cur[i]!=w[i]) cnt++;
                }
                if(cnt==1){
                    q.push(w);
                    visited[w]=visited[cur]+1;
                    if(w==target) return visited[w];
                }
            }
        }
    }
    if(!visited.contains(target) || visited[target]==-1) return 0;
    
    return visited[target];
}