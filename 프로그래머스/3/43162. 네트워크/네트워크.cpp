#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n, false);
    
    for (int i=0; i<n; i++){
        if(!visited[i]){
            queue<int> q;
            answer++;
            q.push(i);
            visited[i]=true;
            
            while(!q.empty()){
                auto curr = q.front();
                q.pop();
                for(int j=0; j<n; j++){
                    if(computers[curr][j]==1 && !visited[j]){
                        q.push(j);
                        visited[j]=true;
                    }
                }
            }
        }
    }
    return answer;
}