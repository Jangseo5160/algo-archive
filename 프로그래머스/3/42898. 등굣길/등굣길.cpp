#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<int>> v(n+1, vector<int>(m+1, 0));
    v[1][1]=1;
    for(auto a:puddles){
        int c=a[0];
        int r=a[1];
        v[r][c] =-1;
    }
    for(int c=1; c<m+1; c++){
        for(int r=1; r<n+1; r++){
            if(r==1 && c==1) continue;
            if(v[r][c]==-1) continue;
            else if(v[r-1][c]==-1 || v[r][c-1]==-1){
                if(c==1 || r==1) v[r][c]=-1;
                else v[r][c]=max(v[r-1][c]%1000000007, v[r][c-1]%1000000007);
            }
            else v[r][c] = v[r-1][c]%1000000007 + v[r][c-1]%1000000007;
        }
    }
    answer = v[n][m]%1000000007;
    if(answer==-1) return 0;
    return answer;
}