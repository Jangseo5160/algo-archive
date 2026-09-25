#include<vector>
#include<queue>

using namespace std;

int solution(vector<vector<int>> maps)
{
    int answer = 0;
    int R = maps.size();
    int C = maps[0].size();
    
    vector<vector<int>> dist(R, vector<int>(C, -1));
    queue<pair<int,int>> q;
    
    int dr[4] = {-1,1,0,0};
    int dc[4] = {0,0,-1,1};
    
    q.push({0,0});
    dist[0][0]=1;
    
    while(!q.empty()){
        auto [r, c] = q.front();
        q.pop();
        
        for(int d=0; d<4; d++){
            int nr = r+dr[d];
            int nc = c+dc[d];
            
            if(nr>=0 && nr<R && nc>=0 && nc<C && maps[nr][nc]==1 && dist[nr][nc]==-1){
                dist[nr][nc] = dist[r][c]+1;
                q.push({nr, nc});
            }
        }
    }    
    return dist[R-1][C-1];
}