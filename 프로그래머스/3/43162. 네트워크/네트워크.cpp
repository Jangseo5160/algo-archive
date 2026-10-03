#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    queue<int> q;
    vector<int> visited(n+1, false);
    
    for(int i=0; i<n; i++){
        if(!visited[i]){
            answer++;
            q.push(i);
            visited[i]=true;
            while(!q.empty()){
                int cur = q.front();
                q.pop();
                
                for(int j=0; j<n; j++){
                    if(computers[cur][j]==1 && !visited[j]){
                        q.push(j);
                        visited[j]=true;
                    }
                }
            }
        }
    }
    return answer;
}